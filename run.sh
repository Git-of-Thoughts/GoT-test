# a) Install dependencies
R -e "install.packages(c('ggplot2', 'readr'), repos='http://cran.rstudio.com/')"

# b) Run all necessary parts of the codebase
Rscript bar_plot_with_p_values.R
