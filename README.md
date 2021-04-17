# SortPeptides
>George Ruck

==Code Logic==

## Python
1. read csv file using pandas library
2. create dataframe for results (peptides and abundance)
3. select values in column (omit nan) and sort (decreasing order)
4. check for length < 3 (only 1/2 peptides)
5. write to new array

## R

*I am not an expert at R efficiency - data.table often more efficient than reading and writing data.frame*

1. read csv file
2. create dataframe
3. select and omit nan -> sort in decreasing
4. write first 3 vales - if only 1/2 values R will write NA

## Difference

Results file will contain NA values if generated with R.