using System;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        char[][] mine = new char[N][];
        char[][] game = new char[N][];

        for (int i = 0; i < N; i++)
        {
            mine[i] = Console.ReadLine().ToCharArray();
        }

        for (int i = 0; i < N; i++)
        {
            game[i] = Console.ReadLine().ToCharArray();
        }

        Func<int, int, object> check = (x, y) =>
        {
            if (mine[x][y] == '*')
            {
                return '*';
            }
            int mineCnt = 0;
            int[][] directions = new int[][] { new int[] { 1, 0 }, new int[] { -1, 0 }, new int[] { 0, -1 }, new int[] { 0, 1 },
                                               new int[] { 1, 1 }, new int[] { 1, -1 }, new int[] { -1, 1 }, new int[] { -1, -1 } };

            foreach (int[] direction in directions)
            {
                int nx = x + direction[0];
                int ny = y + direction[1];
                if (N > nx && nx >= 0 && N > ny && ny >= 0 && mine[nx][ny] == '*')
                {
                    mineCnt++;
                }
            }
            return mineCnt;
        };

        bool flag = true;
        for (int n = 0; n < N; n++)
        {
            for (int m = 0; m < N; m++)
            {
                if (game[n][m] == 'x')
                {
                    object c = check(n, m);
                    if (c.ToString() == "*")
                    {
                        if (flag)
                        {
                            for (int i = 0; i < N; i++)
                            {
                                for (int j = 0; j < N; j++)
                                {
                                    if (mine[i][j] == '*')
                                    {
                                        game[i][j] = '*';
                                    }
                                }
                            }
                            flag = false;
                        }
                    }
                    else
                    {
                        game[n][m] = c.ToString()[0];
                    }
                }
            }
        }

        for (int i = 0; i < N; i++)
        {
            Console.WriteLine(new string(game[i]));
        }
    }
}
