using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApp1
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            TextBoxPostfix.Text = TextBoxInfix.Text.ToPostfix();
            TextBoxPrefix.Text = TextBoxInfix.Text.ToPrefix();

            TreeViewItem newChild = new TreeViewItem();
            newChild.Header = "Test item";
            TreeViewAST.Items.Add(newChild);

        }
    }

    public static class ShuntingYard
    {
        private static readonly Dictionary<string, (string symbol, int precedence, bool isRightAssociative)> stack_Operators
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

                else if (stack_Operators.TryGetValue(token, out var op1))
                {
                    while (stack.Count > 0 && stack_Operators.TryGetValue(stack.Peek(), out var op2))
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
                if (!stack_Operators.ContainsKey(top)) throw new ArgumentException("No matching right parenthesis.");
                output.Add(top);
            }
            return string.Join(" ", output);
        }

        public static string ReverseExpr(string exprexprInfix)
        {
            string[] tokens = exprexprInfix.Split(' ');

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
}
