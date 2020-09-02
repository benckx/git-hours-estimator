<a href="https://paypal.me/benckx/2">
<img src="https://img.shields.io/badge/Donate-PayPal-green.svg"/>
</a>

# About 

Estimate the amount of work spent on a project based on the git commits timestamp.

Algo is based on this (but I couldn't make it work):
https://github.com/kimmobrunfeldt/git-hours

# How To

Navigate to a git project and pipe the result to estimator.py:
```bash
git log --date=iso --pretty=format:'%at' | python3 estimator.py
```
or
```bash
git log --date=iso --pretty=format:'%at' | python3 ../git-hours-estimator/estimator.py
```

Output should be something like:
```
➜  my-super-project git:(master) git log --date=iso --pretty=format:'%at' | python3 ../git-hours-estimator/estimator.py

threshold of 3600 sec.
amount of work (hours): 191
amount of work (days): 23
on a period of (days): 136
nbr of hours/days on this project: 1.4044117647058822

threshold of 7200 sec.
amount of work (hours): 349
amount of work (days): 43
on a period of (days): 136
nbr of hours/days on this project: 2.5661764705882355

threshold of 10800 sec.
amount of work (hours): 470
amount of work (days): 58
on a period of (days): 136
nbr of hours/days on this project: 3.4558823529411766
```
