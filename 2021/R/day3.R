library(tidyr)
library(dplyr)

day3.input <- read.table("day3-input.txt", quote="\"", comment.char="",colClasses = "character")

data <- separate(day3.input,sep = "", col = 1, into = c("x0","x1","x2","x3","x4","x5","x6","x7","x8","x9","x10","x11","x12"))
data <- data[,-c(1)]
data <- as.data.frame(as.matrix(sapply(data, as.numeric)))

# Part 1
one_sum <- colSums(data)
zero_sum <- nrow(data)-one_sum

first_binary <- paste0(as.numeric(one_sum>zero_sum),collapse = "")
second_binary <- paste0(as.numeric(one_sum<zero_sum),collapse = "")

result = strtoi(first_binary,base=2) * strtoi(second_binary,base=2)
(result)

# Part 2
data_most <- data
i = 1
while (nrow(data_most) > 1) {
  one_sum <- colSums(data_most)
  most_common = as.numeric(one_sum[i] >= nrow(data_most)/2)
  keep_index <- which(data_most[,i] == most_common)
  data_most <- data_most[c(keep_index),]
  i = i + 1
}

data_least <- data
i = 1
while (nrow(data_least) > 1) {
  one_sum <- colSums(data_least)
  most_common = as.numeric(one_sum[i] < nrow(data_least)/2)
  keep_index <- which(data_least[,i] == most_common)
  data_least <- data_least[c(keep_index),]
  i = i + 1
}

first_binary <- paste0(data_most,collapse = "")
second_binary <- paste0(data_least,collapse = "")

result = strtoi(first_binary,base=2) * strtoi(second_binary,base=2)
(result)
