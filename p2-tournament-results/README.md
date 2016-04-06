p2: Tournament Results
=============

In fulfillment of Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

###About
 
This project includes a Python module that uses a PostgreSQL database to keep track of players and matches in a Swiss-system tournament.


```
A Swiss-system tournament is a specific kind of sports tournament in which players are not eliminated when they lose a match. Rather, players are paired in each round with oppoents having (approximately) the same win-loss record.
```

>
###Some Assembly Required


You can initiate this project with [Vagrant](https://www.vagrantup.com/) and [Virtual Box](https://www.virtualbox.org/) by executing the following from the command line:

* `vagrant up` inside the `vagrant/` directory
* `vagrant ssh`
* `cd /vagrant/tournament`
* `psql -f tournament.sql`
* `python tournament_test.py`



####Expected Output

The output from executing `python tournament_test.py` should look like this:

```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```

If you run into any issues or find yourself scratching your head, 
feel free to contact me. 
