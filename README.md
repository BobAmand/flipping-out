
Charting data - "flipping-out" exercise at The Iron Yard:

Objectives

Learning Objectives

After completing this assignment, you should understand:

Basic statistics
The use of different plot types
Performance Objectives

After completing this assignment, you should be able to:

Use matplotlib
Use IPython Notebook
Use the statistics module
Details

Deliverables

A Git repo called charting containing at least:
an IPython notebook
a requirements.txt file
Normal Mode

All of the following should be done in an IPython Notebook. You should put necessary imports in the topmost cell(s) of the Notebook, and each task involving code or analysis should be done in its own discrete cell.

Create a function to flip a coin. It is up to you to determine what this returns to signify heads or tails. Then create a function to run a simulation of flipping a coin n number of times, default 216, recording how many heads and tails it has at different intervals. The intervals are exponential, so record at 20, 21, 22, and so on until you reach n. Record the final number as well.

Then make a line plot of the difference between heads and tails at each recorded point, and another with the ratio of heads to tails at each recorded point.

Create these plots again, but as scatter plots with a logarithmic scale for the x-axis.

Write notes about what you observe. Feel free to add more plots to help you.

Now we will look at the mean and standard deviation of these trials of flipping coins. Flip coins as before, but run 20 trials of 216 each.

Use a scatter plot to plot the mean heads/tails ratio at each recorded point, and another scatter plot to plot the standard deviation of the heads/tails ratio at each recorded point. You will want to use a logarithmic scale for the x-axis in both. You may want to do the same for the y-axis with the standard deviation.

Write notes about what you observe. Feel free to add more plots to help you.

Lastly, run 100,000 trials of 100 coin flips each. Plot a histogram of the ratio of heads to total flips for each trial. Run 100,000 trials of 1,000 coin flips each and plot that histogram as well. Lastly, plot a box plot of your results from the 100 coin flip trials and your results from the 1,000 coin flip trials.

What do you observe? Write up your notes.

Hard Mode

Use seaborn and clean up your Notebook file for presentation. Use MarkDown effectively to highlight key observations. (Hint: you can write exponents using the <sup> tag, e.g., 2<sup>16</sup> becomes 216)

Add the mean and standard deviation as text to each applicable histogram.

Additional Resources

matplotlib
seaborn
IPython
Credit

Some assignments adapted from Introduction to Computation and Programming Using Python.
