# Shell-It
Do you have a bunch of tmux helpers? Maybe you constantly need to ssh into various machines. If you have a lot of shell scripts you might find this useful. 

Currently this doesn't work with scripts that take additional arguments, it is only designed to run hard-coded shell scripts.

### Setup:

Install wherever you want. I put `shell-it.sh` in a custom directory called `~/.scripts/`.

Make sure to include `shell-it.sh` in your $PATH. My `.zshrc` includes this:

```zsh
export PATH="$HOME/.scripts:$PATH"
```

Alternatively, make an alias pointing directly to shell-it.sh:

```zsh
alias sh-it="~/path/to/shell-it.sh"
```

### Usage:
By default, Shell-It lists the scripts in your working directory.

```
shell-it.sh
```

Output:
```
Listing scripts in /Users/lesly.kinzel:
1: tunnel.sh
2: tunnel_momo_sql_prod.sh
3: tunnel_rdp_prod_01.sh
4: tunnel_rdp_prod_02.sh
5: tunnel_st_rdp_stage.sh
6: tunnel_st_sql_prod.sh
7: tunnel_st_sql_stage.sh
8: tunnel_ta_sql_prod.sh
Enter number from 1 to 8:
```

Alternatively, you could give it a directory to look into:
```
shell-it.sh /usr/bin/
```
Output:
```
Listing scripts in /usr/bin/:
1: power_report.sh
Enter number from 1 to 1:
```

It also has a `--help` flag.
