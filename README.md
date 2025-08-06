# A.Artifact Appendix

## A.1 Abstract
This artifact contains the Python implementation of TraceSynth as well as all scripts and files necessary for reproducing the experiments described in the paper.
It also provides automation scripts to facilitate experimental reproduction.

## A.2 Artifact Checklist

- Programs: TraceSynth, MemSynth
- Operating System: Linux (e.g., Ubuntu 22.04), Docker
- Hardware Requirements: At least 16GB of RAM, C910 development board
- Experiments: Includes a litmus test suite and C910 execution logs for experimental replay


## A.3 Description

### A.3.1 Hardware Dependencies
All experiments can be reproduced on any PC equipped with at least 16GB of RAM.
While some experiments involve data obtained from a C910 development board, we provide pre-collected execution logs that allow reproduction without access to the board. Additionally, for selected experiments, we offer optional support for execution on a real C910 device.

### A.3.2 Software Dependencies
- A Linux distribution (e.g., Ubuntu 22.04)
- Docker

### A.3.3 Installation
To set up the environment, run the following command:

```
docker container run -it \ --runtime=nvidia --gpus all sa:v1 bash
```


### A.3.4 Dataset

The litmus test suite is located at:`TraceSynth/tests/input/litmus/litmus/non-mixed-size`目录中。
The execution log for Experiments 3 and 4 on the C910 is located at:`TraceSynth/tests/input/chip_execution_logs/C910/chip_log.txt`中。
The execution logs for Experiment 1 on the C910 are located at:`TraceSynth/tests/experiment/results/exp1_log`目录中。


## A.4 Experimental Procedure
To reproduce all experiments (based on the pre-collected C910 logs), navigate to:
```
TraceSynth/tests/experiment
```
Then run:
```
./run.sh
```
The results will be saved in:
```
TraceSynth/tests/results`
```

Due to the complexity of collecting logs directly on the C910 device, Experiments 3 and 4 are only available via log-based reproduction.
However, for Experiment 1 (delay injection), we provide an interface for reproducing results directly on the C910 without relying on pre-collected logs.

To run Experiment 1 directly on the C910, use:
```
./run_with_C910.sh 
```
The results will be saved in:
```
TraceSynth/tests/results`
```

## A.5 Evaluation and Expected Results

All experiment results are stored in `TraceSynth/tests/results`. Below is a description of each result file:

- `exp1_inject.png`: Results of Experiment 1 showing the generalizability of the delay injection algorithm
- `exp1_litmus_trans_results.png`: Results of Experiment 1 showing the additional triggering capability of delay injection
- `exp2_synth_rvwmo_result.txt`: Output file of Experiment 2 synthesizing the RVWMO memory model
- `exp2_synth_rvwmo.log`: Log file of Experiment 2 synthesizing the RVWMO memory model
- `exp3_synth_C910_result.txt`: Output file of Experiment 3 synthesizing the model based on C910 traces
- `exp3_synth_C910.log`: Log file of Experiment 3 synthesizing the model based on C910 traces
- `exp4_synth_C910_post_result.txt`:Output file of Experiment 4 synthesizing with the completed C910 dataset
- `exp4_synth_C910_post.log`: Log file of Experiment 4 synthesizing with the completed C910 dataset
- `exp4_synth_rvwmo_post_result.txt`: Output file of Experiment 4 synthesizing RVWMO with the completed dataset
- `exp4_synth_rvwmo_post.log`: Log file of Experiment 4 synthesizing RVWMO with the completed dataset
