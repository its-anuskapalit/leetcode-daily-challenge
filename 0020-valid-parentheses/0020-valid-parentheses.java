class Solution {

    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for (char currentChar : s.toCharArray()) {
            if (currentChar == '(' || currentChar == '{' || currentChar == '[') {
                stack.push(currentChar);
            }
            else {
                if (stack.isEmpty() || !isMatchingPair(stack.peek(), currentChar)) {
                    return false;
                }

                stack.pop();
            }
        }

        return stack.isEmpty();
    }

   
    private boolean isMatchingPair(char openingBracket, char closingBracket) {
        return (openingBracket == '(' && closingBracket == ')') ||
               (openingBracket == '{' && closingBracket == '}') ||
               (openingBracket == '[' && closingBracket == ']');
    }
}
