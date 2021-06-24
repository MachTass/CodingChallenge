using System;

namespace ReverseLinkedList
{
    public class Node
    {
        private int Data { get; set; }

        private Node Next { get; set; }

        private Node(int data)
        {
            Data = data;
        }
        
        public static string Traverse(Node node)
        {
            var result = String.Empty;
            while (!(node.Next == null))
            {
                result += node.Data + ",";
                node = node.Next;
            }

            result += node.Data;

            return result;
        }

        public static Node CreateList(int[] data)
        {
            var head = new Node(data[0]);
            Node node = head;
            for (var i = 1; i < data.Length; i++)
            {
                var tempNode = new Node(data[i]);
                node.Next = tempNode;
                node = tempNode;
            }

            return head;
        }

        public static Node ReverseList(Node head)
        {
            Node previous = null;
            var current = head;

            while (current.Next != null)
            {
                var next = current.Next;
                current.Next = previous;
                previous = current;
                current = next;
            }

            current.Next = previous;
            
            return current;
        }
    }
}