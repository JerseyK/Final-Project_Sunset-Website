# What is this?

In a prior year, a team named "Wall Street Bets" (Lana Butorovic, Austen Johnson, Joseph Min, and Ryan Schmid) wrote a web app hosted out of [this repo](https://github.com/rws222/fin377-project-site). They used [PyPortfolioOpt](https://pyportfolioopt.readthedocs.io/en/latest/index.html) to plot the efficient frontier and tangency portfolio, and then developed a short quiz to assess the risk aversion parameter for a quadratic utility maximizing investor. With this parameter, they suggested a utlity maximizing portfolio. 

Sadly, their site is no longer working because Heroku, where they hosted it, stopped free services. So I'm porting their project here to demonstrate the use of [Streamlit](https://streamlit.io) for dashboard development and deployment. I've refactored the code in places and added a small tweak to the code to allow for levered portfolios (by shorting the risk free asset).

[You can see this dashboard in action here!](https://donbowen-portfolio-frontier-streamlit-dashboard-app-yentvd.streamlit.app/)

## How to 

### If you want to get this app working on your computer so you can use it, play around with it, or modify it, you need:
1. A working python / Anaconda installation
1. Git 

Then, open a terminal and run these commands one at a time:

```sh
# download files (you can do this via github desktop too)
cd <path to your FIN377 folder> # make sure the cd isn't a repo or inside a repo!
git clone https://github.com/donbowen/portfolio-frontier-streamlit-dashboard.git

# move the terminal to the new folder (adjust next line if necessary)
cd portfolio-frontier-streamlit-dashboard  

# this deletes the .git subfolder, so you can make this your own repo
# MAKE SURE THE cd IS THE portfolio-frontier-streamlit-dashboard FOLDER FIRST!
rm -r -fo .git 

# set up the packages you need for this app to work 
# (YOU CAN SKIP THESE if you have already streamlit-env, or you can 
# give this one a slightly diff name by modifying the environment.yml file)
conda env create -f environment.yml
conda activate streamlit-env

# start the app in a browser window
streamlit run app.py

# open any IDE you want to modify app - spyder > jupyterlab for this
spyder  # and when you save the file, the app website will update
```

### To deploy the site on the web, 
1. Use Github Desktop to make this a repo your own account. 
1. Go to streamlit's website, sign up, and deploy it by giving it the URL to your repo.
1. Wait a short time... and voila!

## Update requests 

1. Easy for me: Add Github action to run `update_data_cache.py` once a month.
1. Easy for anyone: The requirements file has no version restrictions. We should set exact versions.

## Notes

While it seems duplicative to have a `requirements.txt` and a  `environment.yml`, the former is needed by Streamlit and the latter makes setting up a conda environment quickly easy. So keep both. 

---

# Welcome to our [team project website!](https://julioveracruz.github.io/testwebsite/)

This is a website to showcase our final project for FIN 377 - Data Science for Finance course at Lehigh University.

To see the complete analysis file(s) click [here](https://github.com/julioveracruz/testwebsite/blob/main/notebooks/example.ipynb).

Maybe you want a different website them for the project? Consider `minimal-mistakes`:
1. [Go here](https://github.com/mmistakes/mm-github-pages-starter/generate).
2. In the resulting repo, click Settings, then Pages, then make sure the source is the main branch.
3. [The doc site is here](https://mmistakes.github.io/minimal-mistakes/docs/structure/) and will help you customize layouts and figure out how to use it.

## Table of contents
1. [Introduction](#introduction)
2. [Methodology](#meth)
3. [Section 2](#section2)
    1. [Subsection](#subsec2-1)
    2. [Subsection](#subsec2-2)
4. [Analysis Section](#section3)
5. [Summary](#summary)

## Introduction  <a name="introduction"></a>

(The "Introduction" text above is formatted in heading 2 style.) The main goal of this project is to explore *(insert project idea here)*.  

## Methodology <a name="meth"></a>

Here is some code that we used to develop our analysis. Blah Blah. [More details are provided in the Appendix](page2).
 
Note that for the purposes of the website, you have to copy this code into the markdown file and  
put the code inside trip backticks with the keyword `python`.

```python
import seaborn as sns 
iris = sns.load_dataset('iris') 

print(iris.head(),  '\n---')
print(iris.tail(),  '\n---')
print(iris.columns, '\n---')
print("The shape is: ",iris.shape, '\n---')
print("Info:",iris.info(), '\n---') # memory usage, name, dtype, and # of non-null obs (--> # of missing obs) per variable
print(iris.describe(), '\n---') # summary stats, and you can customize the list!
print(iris['species'].value_counts()[:10], '\n---')
print(iris['species'].nunique(), '\n---')
```

Notice that the output does NOT show! **You have to copy in figures and tables from the notebooks.**

## Section <a name="section2"></a>
Blah blah

### Subsection 1 <a name="subsec2-1"></a>
This is a subsection, formatted in heading 3 style

### Subsection 2 <a name="subsec2-2"></a>
This is a subsection, formatted in heading 3 style

## Analysis Section <a name="section3"></a>

Here are some graphs that we created in our analysis. We saved them to the `pics/` subfolder and include them via the usual markdown syntax for pictures.

![](pics/plot1.png)
<br><br>
Some analysis here
<br><br>
![](pics/plot2.png)
<br><br>
More analysis here.
<br><br>
![](pics/plot3.png)
<br><br>
More analysis.

## Summary <a name="summary"></a>

Blah blah



## About the team

<img src="pics/julio.jpg" alt="julio" width="300"/>
<br>
Julio is a senior at Lehigh studying finance.
<br><br><br>
<img src="pics/don2.jpg" alt="don" width="300"/>
<br>
Don is an assistant professor at Lehigh.


## More 

To view the GitHub repo for this website, click [here](https://github.com/donbowen/teamproject).
