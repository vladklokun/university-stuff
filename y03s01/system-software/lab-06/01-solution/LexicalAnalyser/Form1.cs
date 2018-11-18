using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Collections;

namespace LexicalAnalyser
{
    public partial class Form1 : Form
    {
        public string codeText; //считывание содержимого txt файла
        public string codeText1; //считывание содержимого txt файла
        //место хранения текста разбитого на части
        public string[] splitText;
        public string[] splitText1;
        public char[] splitText12;
        
        public Form1()
        {
            InitializeComponent();
        }

       
        private void button1_Click(object sender, EventArgs e)
        {
            List<String> keywords = new List<string>() {
                   "mov",
                   "lea",
                   "xor",
                   "inc",
                   "cmp",
                   "je",
                   "jc",
                   "shr",
                   "jbe",
                   "jmp",
                   "jae",
                   "sub",
                   "push",
                   "add",
                   "pop",
                   "int",
                   "jz"
               };
            //описание объекта класса OpenFileDialog
            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            //фильтр файлов (показывать только .txt)
            openFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
            //если диалог открыт успешно
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    //описание объекта класса StreamReader
                    StreamReader sr = new StreamReader(openFileDialog1.FileName);
                    //считывание в codeText содержимого файла
                    codeText = Convert.ToString(sr.ReadToEnd());                    
                    //вывод содержимого файла в richTextBox
                    richTextBox1.Text = codeText;
                    //закрытие потока
                    sr.Close();

                    //вывод некоторых данных о файле
                    richTextBox2.Clear();
                    richTextBox2.Text = Convert.ToString(openFileDialog1.FileName);


                    //split source code into tokens
                    splitText = codeText.Split(new string[] { "\r\n", "\n", "\r", " ", ".", ";", 
                        "=", "(", ")", "+", "-", "{", "}","[","]" }, StringSplitOptions.RemoveEmptyEntries);

                    // find keywords
                    foreach (string s in splitText)
                    {
                        if (s.Trim() != "" && keywords.Contains(s))
                        {
                                listBox1.Items.Add(s);
                        }
                    }
                    // find variables
                    for (int i=0; i<splitText.Length; i++)
                    {

                        if (keywords.Contains(splitText[i]))
                        {
                        // if keyword is found, next token is assumed to be a variable
                                   listBox2.Items.Add(splitText[i+1]);
                        }                   
                    }
                    // find lables
                    for (int i = 0; i < splitText.Length - 1; i++)
                    {
                        // labels must have a colon in their name
                        if (splitText[i].Contains(":"))
                            listBox3.Items.Add(splitText[i]);
                    }

                }
                catch
                {
                    //Если не получилось открыть файл, выводим сообщение об ошибке
                    MessageBox.Show("Ошибка. Не могу прочесть данные");
                }

            }


        }
             
        //выход из приложения
        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button3_Click(object sender, EventArgs e)
        {
          
           MessageBox.Show("Для работы программы, в текстовых файлах, должна использоваться кодировка UTF-8");
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void listBox2_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void groupBox5_Enter(object sender, EventArgs e)
        {

        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            richTextBox2.Clear();
            listBox1.Items.Clear();
            listBox2.Items.Clear();
            listBox3.Items.Clear();
        }
    }
}

