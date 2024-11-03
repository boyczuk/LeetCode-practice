class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [("", 0, 0)] # current_string, open_count, closed_count

        while stack:
            current_string, open_count, close_count = stack.pop()

            if len(current_string) == 2 * n:  # reached number of pairs expected
                result.append(current_string)

            if open_count < n:
                # Adds different paths to be checked
                stack.append((current_string + "(", open_count + 1, close_count))

            if close_count < open_count:
                stack.append((current_string + ")", open_count, close_count + 1))

        return result