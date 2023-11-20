#! /bin/zsh

for i in {3..75}; do
	file_name="test_problem_$i.py"
	if [ ! -e "$file_name" ]; then
		touch  "$file_name"
	fi
done

#for i in {1..75}; do
#	rm "problem_$i"
#done
