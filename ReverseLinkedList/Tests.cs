using NUnit.Framework;
using Xunit;
using Assert = NUnit.Framework.Assert;

namespace ReverseLinkedList
{
    [TestFixture]
    public class Tests
    {
        [Fact]
        public void TestCreateLinkedList()
        {
            var node = Node.CreateList(new[] {1, 2, 3, 4, 5});
            var result = Node.Traverse(node);
            Assert.AreEqual("1,2,3,4,5", result);
        }

        [Fact]
        public void TestReverseLinkedList()
        {
            var node = Node.CreateList(new[] {1, 2, 3, 4, 5});
            node = Node.ReverseList(node);
            
            Assert.AreEqual("5,4,3,2,1", Node.Traverse(node));
        }
    }
}