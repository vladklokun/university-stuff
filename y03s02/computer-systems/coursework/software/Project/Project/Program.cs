using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
namespace Project
{
    public static class Program
    {
        public static int[,] matrix = new int[75, 75];
        public static int i;
        public static int j;
        public static void Nul(int[,] mtrx)
        {
            for (int i = 0; i < 75; i++)
                for (int j = 0; j < 75; j++)
                    mtrx[i, j] = 0;
        }
        public static void Floyd(int[,] mtrx, int num)
        {
            for (i = 0; i < num; i++)
                for (j = 0; j < num; j++)
                    if (mtrx[i, j] == 0)
                        mtrx[i, j] = 500000;
            for (int k = 0; k < num; k++)
                for (i = 0; i < num; i++)
                    for (j = 0; j < num; j++)
                        if (mtrx[i, j] > mtrx[i, k] + mtrx[k, j])
                            mtrx[i, j] = mtrx[i, k] + mtrx[k, j];
            for (i = 0; i < num; i++)
                mtrx[i, i] = 0;
            for (i = 0; i < 75; i++)
                for (j = 0; j < 75; j++)
                    matrix[i, j] = mtrx[i, j];
        }
        public static int Diametr(int num)
        {
            int d = 0;
            for (i = 0; i < num; i++)
                for (j = 0; j < num; j++)
                    if (d < matrix[i, j]) d = matrix[i, j];
            return d;
        }
        public static double Average_Diametr(int num)
        {
            double md = 0;
            for (i = 0; i < num; i++)
                for (j = 0; j < num; j++)
                    md = md + matrix[i, j];
            md = md / (num * (num - 1));
            return md;
        }
        public static int Degree(int num) 
        {
            int k = 0;
            int s = 0;
            for (i = 0; i < num; i++)
            {
                for (j = 0; j < num; j++)
                    if (matrix[i, j] == 1)
                        k = k + 1;
                if (k > s)
                    s = k;
                k = 0;
            }
            return s;
        }
        public static void Table()
        {
            Console.Write("#\tNumber\tDiametr\tAverage_Diametr\tDegree\tCost\tTraffic\n");
        }
        public static void TableRow(int num, int k)
        {
            Floyd(matrix, num);
            Console.Write("{0:D}\t{1:D}\t{2:D}\t{3:f}\t\t{4:D}\t{5:D}\t{6:f}\t\n", k, num, Diametr(num), Average_Diametr(num), Degree(num), Diametr(num) * Degree(num) * num, 2 * Average_Diametr(num) / Degree(num));
        }
        public static void WriteFile(int num, int k, string topology)
        {
            using (StreamWriter file = new StreamWriter(topology, true))
            {
                file.WriteLine(k + "\t" + num + "\t" + Diametr(num) + "\t" + Average_Diametr(num) + "\t" + Degree(num) + "\t" + Diametr(num) * Degree(num) * num + "\t" + 2 * Average_Diametr(num) / Degree(num));
            }
        }
        static void Main()
	    {
            Console.WindowWidth = 151;//Console.LargestWindowWidth;
            Console.WindowHeight = 65; //Console.LargestWindowHeight;
            /*Nul(matrix);
            FillMatrix_24(matrix);
            MatrixMirror(matrix);
            for (i = 0; i < 7; i++)
            {
                for (j = 0; j < 7; j++)
                    Console.Write(matrix[i, j] + " ");
                Console.WriteLine();
            }
            Console.WriteLine();
            Nul(matrix);
            Test(matrix);
            for (i = 0; i < 7; i++)
            {
                for (j = 0; j < 7; j++)
                    Console.Write(matrix[i, j] + " ");
                Console.WriteLine();
            }
           */
            Console.Write("\n                              Line                              \n\n");
            Table();
            int k = 1;
            int num = 0;
            do
            {
                Nul(matrix);
                num = 7 * k;
                for (int x = 0; x < k; x++)
                {
                    int i = 7 * x;
                    matrix[i + 0, i + 1] = 1;
                    matrix[i + 0, i + 2] = 1;
                    matrix[i + 0, i + 3] = 1;
                    matrix[i + 0, i + 4] = 1;
                    matrix[i + 1, i + 0] = 1;
                    matrix[i + 1, i + 2] = 1;
                    matrix[i + 1, i + 3] = 1;
                    matrix[i + 1, i + 5] = 1;
                    matrix[i + 2, i + 0] = 1;
                    matrix[i + 2, i + 1] = 1;
                    matrix[i + 2, i + 4] = 1;
                    matrix[i + 2, i + 5] = 1;
                    matrix[i + 2, i + 6] = 1;
                    matrix[i + 3, i + 0] = 1;
                    matrix[i + 3, i + 1] = 1;
                    matrix[i + 3, i + 4] = 1;
                    matrix[i + 3, i + 5] = 1;
                    matrix[i + 4, i + 0] = 1;
                    matrix[i + 4, i + 2] = 1;
                    matrix[i + 4, i + 3] = 1;
                    matrix[i + 4, i + 5] = 1;
                    matrix[i + 4, i + 6] = 1;
                    matrix[i + 5, i + 1] = 1;
                    matrix[i + 5, i + 2] = 1;
                    matrix[i + 5, i + 3] = 1;
                    matrix[i + 5, i + 4] = 1;
                    matrix[i + 5, i + 6] = 1;
                    matrix[i + 6, i + 2] = 1;
                    matrix[i + 6, i + 4] = 1;
                    matrix[i + 6, i + 5] = 1;
 
                    matrix[i + 8, i + 2] = 1;
                    matrix[i + 10, i + 4] = 1;
                    matrix[i + 12, i + 6] = 1;
                    matrix[i + 2, i + 8] = 1;
                    matrix[i + 4, i + 10] = 1;
                    matrix[i + 6, i + 12] = 1;

                }
                TableRow(num, k);
                WriteFile(num, k, @"Line.txt");
                k++;
            }
            while (num < 50);

            Console.Write("\n                              Star                              \n\n");
            Table();
            k = 1;
            num = 0;
            do
            {
                Nul(matrix);
                num = 7 * k + 1;
                for (int x = 0; x < k; x++)
                {
                    int i = 7 * x;
                    matrix[i + 1, i + 0]=1;
                    matrix[i + 1, i + 2]=1;
                    matrix[i + 1, i + 3]=1;
                    matrix[i + 1, i + 4]=1;
                    matrix[i + 1, i + 5]=1;
                    matrix[i + 2, i + 1]=1;
                    matrix[i + 2, i + 3]=1;
                    matrix[i + 2, i + 4]=1;
                    matrix[i + 2, i + 6]=1;
                    matrix[i + 3, i + 1]=1;
                    matrix[i + 3, i + 2]=1;
                    matrix[i + 3, i + 6]=1;
                    matrix[i + 3, i + 7]=1;
                    matrix[i + 4, i + 1]=1;
                    matrix[i + 4, i + 2]=1;
                    matrix[i + 4, i + 5]=1;
                    matrix[i + 4, i + 6]=1;
                    matrix[i + 5, i + 1]=1;
                    matrix[i + 5, i + 4]=1;
                    matrix[i + 5, i + 6]=1;
                    matrix[i + 5, i + 7]=1;
                    matrix[i + 6, i + 2]=1;
                    matrix[i + 6, i + 3]=1;
                    matrix[i + 6, i + 4]=1;
                    matrix[i + 6, i + 5]=1;
                    matrix[i + 6, i + 7]=1;
                    matrix[i + 7, i + 3]=1;
                    matrix[i + 7, i + 5]=1;
                    matrix[i + 7, i + 6]=1;

                    matrix[0, i + 1]=1;
                    matrix[i + 1, 0] = 1;
                }
                TableRow(num, k);
                WriteFile(num, k, @"Star.txt");
                k++;
            }
            while (num < 50);

            Console.Write("\n                              Ring                              \n\n");
            Table();
            k = 1;
            num = 0;
            do
            {
                Nul(matrix);
                num = 7 * k;

                for (int x = 0; x < k; x++)
                {
                    int i = 7 * x;
                    matrix[i + 0, i + 1] = 1;
                    matrix[i + 0, i + 2] = 1;
                    matrix[i + 0, i + 3] = 1;
                    matrix[i + 0, i + 4] = 1;
                    matrix[i + 1, i + 0] = 1;
                    matrix[i + 1, i + 2] = 1;
                    matrix[i + 1, i + 3] = 1;
                    matrix[i + 1, i + 5] = 1;
                    matrix[i + 2, i + 0] = 1;
                    matrix[i + 2, i + 1] = 1;
                    matrix[i + 2, i + 4] = 1;
                    matrix[i + 2, i + 5] = 1;
                    matrix[i + 2, i + 6] = 1;
                    matrix[i + 3, i + 0] = 1;
                    matrix[i + 3, i + 1] = 1;
                    matrix[i + 3, i + 4] = 1;
                    matrix[i + 3, i + 5] = 1;
                    matrix[i + 4, i + 0] = 1;
                    matrix[i + 4, i + 2] = 1;
                    matrix[i + 4, i + 3] = 1;
                    matrix[i + 4, i + 5] = 1;
                    matrix[i + 4, i + 6] = 1;
                    matrix[i + 5, i + 1] = 1;
                    matrix[i + 5, i + 2] = 1;
                    matrix[i + 5, i + 3] = 1;
                    matrix[i + 5, i + 4] = 1;
                    matrix[i + 5, i + 6] = 1;
                    matrix[i + 6, i + 2] = 1;
                    matrix[i + 6, i + 4] = 1;
                    matrix[i + 6, i + 5] = 1;

                    matrix[i + 8, i + 2] = 1;
                    matrix[i + 10, i + 4] = 1;
                    matrix[i + 12, i + 6] = 1;
                    matrix[i + 2, i + 8] = 1;
                    matrix[i + 4, i + 10] = 1;
                    matrix[i + 6, i + 12] = 1;

                }
                matrix[1, k * 7 - 5] = 1;
                matrix[3, k * 7 - 3] = 1;
                matrix[5, k * 7 - 1] = 1;

                matrix[k * 7 - 5, 1] = 1;
                matrix[k * 7 - 3, 3] = 1;
                matrix[k * 7 - 1, 5] = 1;
                TableRow(num, k);
                WriteFile(num, k, @"Ring.txt");
                k++;
            }
            while (num < 50);
		    Console.Read();

	}
    }
}
