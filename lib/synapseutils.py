#!/usr/bin/env python


import tempfile
import synapseclient
import os

#modified from  Larsson's code
#https://github.com/larssono/Analysis_helpers/blob/master/synapseHelpers.py
def query2df(queryContent, filterSynapseFields=True):
    """Converts the returned query object from Synapse into a Pandas DataFrame
    
    Arguments:
    - `queryContent`: content returned from query
    - `filterSynapseFields`: Removes Synapse properties of the entity returned with "select * ..."
    """
    import pandas as pd
    queryContent = pd.DataFrame(queryContent['results'])
    #Remove the unecessary lists and 'entity' in names  (this should be fixed on Synapse!)
    for key in queryContent.keys():
        newkey=key.replace('entity.', '')
        temp_list = []
        #list comprehension not feasible as multiple IF conditions are checked
        for item in queryContent[key]:
        	if type(item) is list:
        		temp_list.append(item[0])
        	else:
        		temp_list.append(item) 
        queryContent[newkey] = pd.Series(temp_list)
        del queryContent[key]
    return queryContent



def push_DF_to_synLeaderboard(df, wikiEntity=None, subPageId=None, syn=None, prefixText=None, suffixText=None):
    df = df.reset_index()
    if prefixText:
        wikiText = "%s\n\n" % prefixText
    else:
        wikiText = ''
    ncols = df.shape[1]
    nrows = df.shape[0]
    mod_colnames = map(lambda x: x.replace('_', '-'), df.columns.values)
    wikiText += "|%s|\n" %  ('|'.join(mod_colnames))
    wikiText += "|%s|\n" %  ( '|'.join(['--'] * ncols))
    
    for row in df.iterrows():
        values = row[1].values
        wikiText += "|%s|\n" % ('|'.join(map(str,values)))
    if suffixText:
        wikiText += "%s\n" % suffixText

    #just return the text
    if wikiEntity is None and syn is None:
    	return wikiText
    else:
    	wiki = syn.getWiki(wikiEntity, subpageId=subPageId)
        wiki['markdown'] = wikiText
        syn.store(wiki)
        return wikiText


def pushToSynapse(syn, value, parentId, fileName = None):
    """
    given a file or a string push the same to synaspe under the given synapseId

    """
    temp_file = tempfile.NamedTemporaryFile(mode='w+t',prefix='command_line_used_', suffix='.txt', delete=False)
    temp_file.write(value)
    temp_file.close()

    if fileName is None:
        fileName = os.path.basename(temp_file.name)
    
    syn_temp_file = syn.store(synapseclient.File(temp_file.name, parentId=parentId, name=fileName))
    return syn_temp_file.id

