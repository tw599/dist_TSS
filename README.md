# About

- Uses gene annotation files (.csv/.xlsx) to generate Distance to Transcription Start Site (TSS) plots.
- Plots represent Distance (in kb) versus the Number of Peaks/Sites at a specific distance.
- Specifically useful for profiling the Distance to TSS profiles for annotated ChIP-Seq, ATAC-Seq, HiC peaks.

![](/TSSplot.png)
<br><br><br>

# Pre-Requisites

Install python modules: *pandas*,*matplotlib*,*argparse*,*numpy*.

```
pip install pandas matplotlib argparse numpy
```

Input annotation file must contain a Distance to TSS column that can be read and interpreted by the tool.

Example: Use annotation files generated by [HOMER](http://homer.ucsd.edu/homer/ngs/annotation.html)

# Usage

```
python dist_TSS.py [-h] [--bin_width BIN_WIDTH] [--color COLOR]
                   [--file_format {pdf,png}]
                   input_file output_file
```
