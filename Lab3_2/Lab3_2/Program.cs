using System;

namespace Lab3_2
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] myArray = new int[7, 7];
            Random rand = new Random();
            Console.WriteLine("Начальный массив: ");
            for (int i = 0; i < myArray.GetLength(0); i++)
            {
                for (int j = 0; j < myArray.GetLength(1); j++)
                {
                    myArray[i, j] = rand.Next(10);
                    Console.Write(" " + myArray[i, j]);
                }
                Console.WriteLine();
            }
            Console.WriteLine("Перевернутый массив: ");
            for (int i = 0; i < myArray.GetLength(0); i++)
            {
                for (int j = myArray.GetLength(1) - 1; j >= 0; j--)
                {
                    Console.Write(" " + myArray[j, i]);
                }
                Console.WriteLine();
            }
        }
    }
}