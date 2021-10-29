import subprocess

genome_reference_fasta="reference_genome.fasta"


def Read_In_Bams(bam_list=None,target_file=None,genome_reference_fasta=None,rdata_file_prefix=None):
    read_in_bam=" ".join([
        "Rscript",
        "ReadInBams.R",
        "--bams",bam_list,
        "--bed",target_file,
        "--fasta", genome_reference_fasta,
        "--out",rdata_file_prefix
    ])
    execute_read_in_bam=subprocess.call(read_in_bam,shell=True)
    
def Identify_Failures(r_data=None,exons=None,failures_prefix=None):
    identify_failure=" ".join([
        "Rscript",
        "IdentifyFailures.R",
        "--Rdata",r_data,
        "--exons",exons,
        "--custom TRUE",
        "--out",failures_prefix
    ])
    execute_identify_failures=subprocess.call(identify_failure,shell=True)

def Make_Cnv_Calls(r_data=None,exons=None,call_cnvs_prefix=None,plot_folder=None):
    make_cnv_call=" ".join([
        "Rscript",
        "makeCNVcalls.R",
        "-Rdata",r_data,
        "--exons",exons,
        "--custom TRUE",
        "--out",call_cnvs_prefix,
        "plot All",
        "plotFolder",plot_folder
    ])
    execute_make_cnv_calls=subprocess.call(make_cnv_call,shell=True)

def Run_Shiny(cnv_calls_r_data=None):
    run_shiny=" ".join([
        "Rscript",
        "runShiny.R",
        "--Rdata",cnv_calls_r_data
    ])
    execute_run_shiny=subprocess.call(run_shiny,shell=True)

Read_In_Bams("decon_test_files","decon_test_files/test_Target_Regions.bed",genome_reference_fasta,"DECoNtest")
Identify_Failures("DECoNtest.RData","decon_test_files/test_customNumbering.txt","DECoNtest")
Make_Cnv_Calls("DECoNtest.RData","decon_test_files/test_customNumbering.txt","DECoNtestCalls","DECoNtestPlots")
Run_Shiny("DECoNtestCalls.RData")
