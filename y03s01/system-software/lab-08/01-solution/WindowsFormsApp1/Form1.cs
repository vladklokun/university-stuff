using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBoxPostfix.Text = textBoxInfix.Text.ToPostfix();
            textBoxPrefix.Text = textBoxInfix.Text.ToPrefix();

            var splitPrefix = textBoxPrefix.Text.Split(' ');
            treeView1.Nodes.Clear();
            treeView1.ASTBuild(splitPrefix);
            treeView1.ExpandAll();
        }
    }

    public static class ShuntingYard
    {
        private static readonly Dictionary<string, (string symbol, int precedence, bool isRightAssociative)> operators
            = new (string symbol, int precedence, bool isRightAssociative)[] {
            ("^", 4, true),
            ("*", 3, false),
            ("/", 3, false),
            ("+", 2, false),
            ("-", 2, false)
        }.ToDictionary(op => op.symbol);

        public static string ToPostfix(this string exprInfix)
        {
            string[] tokens = exprInfix.Split(' ');

            var stack = new Stack<string>();
            var output = new List<string>();

            foreach (string token in tokens)
            {
                if (Double.TryParse(token, System.Globalization.NumberStyles.Any, System.Globalization.CultureInfo.InvariantCulture, out _))
                {
                    output.Add(token);
                }

                else if (operators.TryGetValue(token, out var op1))
                {
                    while (stack.Count > 0 && operators.TryGetValue(stack.Peek(), out var op2))
                    {
                        int c = op1.precedence.CompareTo(op2.precedence);

                        if (c < 0 || !op1.isRightAssociative && c <= 0)
                        {
                            output.Add(stack.Pop());
                        }
                        else
                        {
                            break;
                        }
                    }
                    stack.Push(token);
                }
                else if (token == "(")
                {
                    stack.Push(token);
                }
                else if (token == ")")
                {
                    string top = "";
                    while (stack.Count > 0 && (top = stack.Pop()) != "(")
                    {
                        output.Add(top);
                    }
                    if (top != "(") throw new ArgumentException("No matching left parenthesis.");
                }
            }
            while (stack.Count > 0)
            {
                var top = stack.Pop();
                if (!operators.ContainsKey(top)) throw new ArgumentException("No matching right parenthesis.");
                output.Add(top);
            }
            return string.Join(" ", output);
        }

        public static string ReverseExpr(string exprInfix)
        {
            string[] tokens = exprInfix.Split(' ');

            Array.Reverse(tokens);

            var reversed = string.Join(" ", tokens);

            var res = reversed.Replace('(', '@').Replace(')', '(').Replace('@', ')');

            return res;
        }

        public static string ToPrefix(this string expr)
        {
            return ReverseExpr(ToPostfix(ReverseExpr(expr)));
        }
    }

    public static class AbstractSyntaxTree
    {
        public static void ASTBuild(this TreeView treeView, string[] expr)
        {
            treeView.Nodes.Add(expr[0]);
            var curNode = treeView.Nodes[0];
            
            for (int i = 1; i < expr.Length; i++)
            {
               curNode.ASTInsert(expr[i]);
            }
            
        }

        public static void ASTInsert(this TreeNode treeNode, string term)
        {
            treeNode.Nodes.Add(term);
        }
    }
}
