#! /bin/zsh

for i in {5..75}; do
	file_name="problem_$i.py"
	if [ ! -e "$file_name" ]; then
		touch  "$file_name"
	fi
done

#for i in {1..75}; do
#	rm "problem_$i"
#done
