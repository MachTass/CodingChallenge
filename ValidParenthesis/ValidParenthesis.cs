using System;

namespace ValidParenthesis
{
    public class ValidParenthesis
    {
        public static bool isValid(string input)
        {
            int counter = 0;

            foreach (char character in input)
            {
                if (character.Equals('('))
                    counter++;
                else if (character.Equals(')'))
                    counter--;

                if (counter < 0)
                    return false;
            }
            return counter == 0;
        }
    }
}