using NUnit.Framework;

namespace ValidParenthesis
{
    [TestFixture]
    public class Tests
    {
        [TestCase("", true)]
        [TestCase("()", true)]
        [TestCase(")(", false)]
        [TestCase("askdl;jhf", true)]
        [TestCase(")(()))", false)]
        [TestCase("(", false)]
        [TestCase("(())((()())())", true)]
        [TestCase("({))(((}())())", false)]
        [TestCase("[())((()())()]", false)]
        [TestCase("<())((()())()>", false)]
        [TestCase("(as)()kd((l();jh)f)", true)]
        public void IsValidTest(string input, bool result)
        {
            Assert.AreEqual(result, ValidParenthesis.isValid(input));
        }
    }
}