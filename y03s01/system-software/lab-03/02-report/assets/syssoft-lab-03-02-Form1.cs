using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace syssoft_lab_03
{
    public partial class Form1 : Form
    {
        System.Double op1 = 0;
        System.Double op2 = 0;
        System.Double res = 0;

        String msg_InvalidArg = "Invalid argument. Please re-check input.";
        String caption = "Invalid argument";
        public Form1()
        {
            InitializeComponent();
        }
        private bool validate_arguments(String op1_as_str, String op2_as_str)
        {
            bool res1 = Double.TryParse(textBox1.Text, out op1);
            if (!res1)
            {
                MessageBox.Show(this, msg_InvalidArg, caption);
                return false;
            }
            bool res2 = Double.TryParse(textBox2.Text, out op2);
            if (!res2)
            {
                MessageBox.Show(this, msg_InvalidArg, caption);
                return false;
            }
            return (res1 && res2);
        }
        private void button1_Click(object sender, EventArgs e)
        {
            label3.Text = "TBD.";
            if (validate_arguments(textBox1.Text, textBox2.Text) == true)
            {
                res = op1 + op2;
                label3.Text = res.ToString();
            }
        }
        private void button2_Click(object sender, EventArgs e)
        {
            label3.Text = "TBD.";
            if (validate_arguments(textBox1.Text, textBox2.Text))
            {
                res = op1 - op2;
                label3.Text = res.ToString();
            }
        }
        private void button3_Click(object sender, EventArgs e)
        {
            label3.Text = "TBD.";
            if (validate_arguments(textBox1.Text, textBox2.Text))
            {
                res = op1 * op2;
                label3.Text = res.ToString();
            }
        }
        private void button4_Click(object sender, EventArgs e)
        {
            label3.Text = "TBD.";
            if (validate_arguments(textBox1.Text, textBox2.Text))
            {
                try
                {
                    res = op1 / op2;
                    label3.Text = res.ToString();
                }
                catch (DivideByZeroException)
                {
                    MessageBox.Show("Cannot divide by zero!");
                    label3.Text = "NaN";
                }
            }
        }
        private void button5_Click(object sender, EventArgs e)
        {
            label3.Text = "TBD.";
            if (validate_arguments(textBox1.Text, textBox2.Text))
            {
                res = Math.Pow(op1, op2);
                label3.Text = res.ToString();
            }
        }
        private void button6_Click(object sender, EventArgs e)
        {
            label3.Text = "TBD.";
            if (validate_arguments(textBox1.Text, textBox2.Text))
            {
                res = Math.Log(op1, op2);
                label3.Text = res.ToString();
            }
        }
    }
}
