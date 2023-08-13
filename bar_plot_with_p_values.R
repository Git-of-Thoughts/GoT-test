# Load necessary libraries
library(ggplot2)
library(readr)

# Function to load data
load_data <- function(file_path) {
  data <- read_csv(file_path)
  return(data)
}

# Function to calculate p-values
calculate_p_values <- function(data) {
  categories <- unique(data$category)
  p_values <- sapply(categories, function(cat) {
    t.test(data$value[data$category == cat])$p.value
  })
  return(p_values)
}

# Function to create bar plot with p-values
create_bar_plot <- function(data, p_values) {
  plot <- ggplot(data, aes(x = category, y = value)) +
    geom_bar(stat = "identity") +
    geom_text(aes(label = round(p_values, 3)), vjust = -0.5)
  return(plot)
}

# Main script
file_path <- "data.csv"  # Replace with your CSV file path
data <- load_data(file_path)
p_values <- calculate_p_values(data)
plot <- create_bar_plot(data, p_values)
print(plot)
