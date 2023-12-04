class Solution:
    def compress(self, chars: list[str]) -> int:
        
        unique_chars = []
        count = 0
        
        previous_char = chars[0]

        for index, char in enumerate(chars):

            if index != 0:
                previous_char =  chars[index - 1]

            if previous_char == char:
                count += 1

            else:
                unique_chars.append(previous_char)
                if count > 1:
                    if count > 10:
                        unique_chars.extend(list(str(count)))
                    else:
                        unique_chars.append(str(count))
                count = 1

            if index == len(chars) - 1:
                unique_chars.append(char)
                if count > 1:
                    if count > 10:
                        unique_chars.extend(list(str(count)))
                    else:
                        unique_chars.append(str(count))         

        chars[:len(unique_chars)] = unique_chars

        return len(unique_chars)
    
