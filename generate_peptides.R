#set wd and read data (peptide = rownames)
setwd("D:/Code/Trier_peptides/SortPeptides")
file <- "peptides_1"
df <- read.csv(paste(file,".csv",sep = ""),row.names = 1)

#allocate space for results peptides
df_result <- data.frame(Peptide1 = character(ncol(df)),
                        Peptide2 = character(ncol(df)),
                        Peptide3 = character(ncol(df)))

#allocate space for abundance of peptides
df_nresult <- data.frame(Peptide1 = integer(ncol(df)),
                         Peptide2 = integer(ncol(df)),
                         Peptide3 = integer(ncol(df)))

#assign colnames as rownames (results)
cols <- colnames(df)
row.names(df_result) <- cols
row.names(df_nresult) <- cols
#peptides <- rownames(df)

for (col in cols){
  
  #select non null values 
  #order values decreasing
  data <- na.omit(df[,col,drop = FALSE])
  data <- data[order(data,decreasing = TRUE),drop = FALSE,]
  
  #add relevant data (add na value automatically)
  df_result[col,] <- rownames(data)[1:3]
  df_nresult[col,] <- data[1:3,]
  
}

#write data to file
write.csv(df_result,paste(file,"_results_R.csv",sep = ""))