#!/usr/bin/env bash
aoc_dir="$HOME/Working/advent-of-code"

year=$1
day=$2

cd $aoc_dir

new_dir=$year/day$day
echo "making new dir: $new_dir"
mkdir $new_dir

cp $aoc_dir/template/* $new_dir/

mv $new_dir/day.py $new_dir/day$day.py
mv $new_dir/day.ipynb $new_dir/day$day.ipynb