#!/usr/bin/env python



import os
import sys
import argparse



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
    user_args = parser.parse_args()
    
     
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    
    
    for run_func in user_args.run_funcs:
        func_to_run = translator_userArg_to_funcName.get(run_func,None)
        func_to_run = eval('bamUtils.%s' % func_to_run)
        bam_stats = parallel.parallelize_func_singe_input(func_to_run,user_args.bam_files,num_cores=user_args.num_cores)
    

    print bam_stats

if __name__ == "__main__":
    main()
    








        
            
    
    
    






