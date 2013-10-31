#!/usr/bin/env python



import os
import sys
import argparse
import functools
import pandas 



##updating the library look up path
dir = os.path.dirname(__file__)
sys.path.append(os.path.join(dir,'../lib'));
import bamUtils
import utils
import parallel



translator_userArg_to_funcName = {
                                    'toBigWig'  : 'bam_to_bigWig',
                                    'getStats'   : 'get_bamStats'
                                }



def main():
    SUB = 'main'
    description  =  """
                    ######
                    Script to analyze BAMs
                    ######
                    """
    
    available_functions  = 'Functions available: \n'
    for count,funcs in enumerate(translator_userArg_to_funcName.keys()):
        available_functions +='%d: %s\n' % (count+1,funcs)
    description += '\n\n' + available_functions    
    
    #user command line args processing
    parser = argparse.ArgumentParser(description=description,add_help=True)
    parser.add_argument('-b','--bams',dest='bam_files',nargs='+',default=None,metavar='',help='list of bam/sam files')
    parser.add_argument('-nc','--num_cores',dest='num_cores',default=1,type=int,metavar='',help='number of slots to use')
    parser.add_argument('-funcs', '--run_funcs',dest='run_funcs',nargs='+',default=None,metavar='',help='list of progs to run')
    parser.add_argument('-f', '--force_run',dest='force_run',default=False,action='store_true',help='list of progs to run')
    parser.add_argument('-o', '--output_dir',dest='output_dir',default=None,help='dir to place the output in..<default: same as input file dir>')
    user_args = parser.parse_args()
    
     
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    
    #create output dir if not exists
    if user_args.output_dir:
        user_args.output_dir = os.path.abspath(user_args.output_dir)
        if not os.path.exists(user_args.output_dir):
            os.makedirs(user_args.output_dir)
        
    
    
    
    for run_func in user_args.run_funcs:
        func_to_run = translator_userArg_to_funcName.get(run_func,None)
        func_to_run = eval('bamUtils.%s' % func_to_run)
        #create a partial func
        func_to_run = functools.partial(func_to_run,force=user_args.force_run,output_dir=user_args.output_dir)
        result = parallel.parallelize_func_singe_input(func_to_run,user_args.bam_files,num_cores=user_args.num_cores)
    

    
    #TO BE MADE MORE ROBUST
    #will error if there is any func arg other than 'getStats'
    df = pandas.DataFrame.from_dict(result)
    df = df.set_index(['bamFile'])
    print df
    
if __name__ == "__main__":
    main()
    








        
            
    
    
    






