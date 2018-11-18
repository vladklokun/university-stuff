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
        public string codeText; //сюда будем считывать содержимое txt файла
        public string codeText1; //сюда будем считывать содержимое txt файла
        //здесь будем хранить текст разбитый на части
        public string[] splitText;
        public string[] splitText1;
        public char[] splitText12;
        
        public Form1()
        {
            InitializeComponent();
        }

       
        private void button1_Click(object sender, EventArgs e)
        {
            //описываем объект класса OpenFileDialog
            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            //устанавливаем фильтр файлов (показывать только .txt)
            openFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
            //если диалог открыт удачно
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    //описываем объект класса StreamReader
                    StreamReader sr = new StreamReader(openFileDialog1.FileName);
                    //считываем в codeText содержимое файла
                    codeText = Convert.ToString(sr.ReadToEnd());                    
                    //выводим содержимое файла в richTextBox
                    richTextBox1.Text = codeText;
                    //закрываем поток
                    sr.Close();

                    //выведем некоторые данные о файле
                    richTextBox2.Clear();
                    richTextBox2.Text = Convert.ToString(openFileDialog1.FileName);

                 
                    //разобъем текст в строке на части
                    splitText = codeText.Split(new Char[] { ' ', ',', '.', ';', ':',
                        '=', '(', ')', '+', '-', '{', '}','[',']' });
                    
#region Поиск ключевых слов
                    foreach (string s in splitText)
                    {
                  
                        //Trim() yдаляет все начальные и конечные знаки пробела из текущего объекта String
                        if (s.Trim() != "" && s == "int" || s == "double" || s == "float"
                            || s == "char" || s == "string")
                        {
                            listBox1.Items.Add(s);
                        }

                    }
#endregion
#region Поиск  переменных
                 
                    for (int i=0; i<splitText.Length; i++)
                    {

                        if (splitText[i] == "int" || splitText[i] == "float"
                            || splitText[i] == "double" || splitText[i] == "char" || splitText[i] == "string")
                        {
                        //если нашли ключевое слово, выводим следующий после него элемент массива
                                   listBox2.Items.Add(splitText[i+1]);
                              //проверяем нет ли второй переменной после ключевого слова     
                            /*if (splitText[i + 3] != "\0")
                                   {
                                      
                                           listBox2.Items.Add(splitText[i + 3]);
                                      
                                   }*/
                               
                        }
                                           
                    }
                           
                                      
#endregion
#region Поиск  функций
                    //разбиваем текст
                   splitText1 = codeText.Split(new Char[] { ' ', '{', '}','(', ')' });
                    for (int i = 0; i < splitText1.Length; i++)
                    {
                        if (splitText1[i]== "void" )
                        listBox3.Items.Add(splitText1[i + 1]);
                    }
#endregion
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
          
           MessageBox.Show("Для корректной работы программы, в загружаемых текстовых файлах, должна использоваться кодировка UTF-8");
        }

        
        
    }
}

