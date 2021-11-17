# programmatic_chart_poc
POC for working with looping through ggplot charts and saving to PNG files

# POC steps
1. Used play by play dataset for NFL games (2021 season).
2. Wrangle data to be a player + date grain, total pass attempts per day.
    - For POC, assume this step is done outside of plotting script. Data manipulation does not play into how long it takes to produce plots.
3. Loop through each player who has attempted a pass, plot by day.
4. Save plot for each player as a .png file.

# Outcome
- Solution needed to scale. 88 plots exported in just under 40 seconds is **too slow**.
- Lots of potential to streamline plot building, potentially multithread, etc.
- Dataset being as clean and ready to use as possible will streamline program for plotting significantly, but is not an obvious performance improvement.

# Example plots
![Aaron Rodgers](/plots/AaRodgers.png)
![Justin Fields](/plots/JFields.png)
![Joe Burrow](/plots/JBurrow.png)
![Dak Prescott](/plots/DPrescott.png)
