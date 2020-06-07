import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    private boolean[][] site = null;
    private final WeightedQuickUnionUF ufPercolation;
    private final WeightedQuickUnionUF ufFilled;
    private final int n;
    private final int sink;
    private int opened = 0;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(final int n) {
        if (n < 1) {
            throw new IllegalArgumentException();
        }
        site = new boolean[n][n];
        this.n = n;
        for (int i = 0; i < site.length; i++) {
            for (int j = 0; j < site.length; j++) {
                site[i][i] = false;
            }
        }
        final int nSquared = n * n;
        ufPercolation = new WeightedQuickUnionUF(nSquared + 2);
        ufFilled = new WeightedQuickUnionUF(nSquared + 1);
        sink = nSquared + 2;
        for (int i = 1; i <= n; i++) {
            ufPercolation.union(0, i);
            ufPercolation.union(sink - 1, sink - i - 1);
            ufFilled.union(0, i);
        }
    }

    // opens the site (row, col) if it is not open already
    public void open(final int row, final int col) {
        validateArgs(row, col);
        if (!site[row - 1][col - 1]) {
            site[row - 1][col - 1] = true;
            opened += 1;
        }
        final int p = toIndex(row, col);

        if (col < this.n && isOpen(row, col + 1)) {
            ufPercolation.union(p, toIndex(row, col + 1));
            ufFilled.union(p, toIndex(row, col + 1));
        }
        if (row < this.n && isOpen(row + 1, col)) {
            ufPercolation.union(p, toIndex(row + 1, col));
            ufFilled.union(p, toIndex(row + 1, col));
        }
        if (col > 1 && isOpen(row, col - 1)) {
            ufPercolation.union(p, toIndex(row, col - 1));
            ufFilled.union(p, toIndex(row, col - 1));
        }
        if (row > 1 && isOpen(row - 1, col)) {
            ufPercolation.union(p, toIndex(row - 1, col));
            ufFilled.union(p, toIndex(row - 1, col));
        }
    }

    private int toIndex(final int row, final int col) {
        return ((row - 1) * n) + col;
    }

    private void validateArgs(final int row, final int col) {
        if (1 > row || row > site.length || 1 > col || col > site.length) {
            throw new IllegalArgumentException();
        }
    }

    // is the site (row, col) open?
    public boolean isOpen(final int row, final int col) {
        validateArgs(row, col);
        return site[row - 1][col - 1];
    }

    // is the site (row, col) full?
    public boolean isFull(final int row, final int col) {
        validateArgs(row, col);
        return isOpen(row, col) && (ufFilled.find(0) == ufFilled.find(toIndex(row, col)));
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return opened;
    }

    // does the system percolate?
    public boolean percolates() {
        if (n == 1)
            return isOpen(1, 1);
        return ufPercolation.find(0) == ufPercolation.find(sink - 1);
    }

    public void printSite() {
        StdOut.printf("%n");
        for (int i = 0; i < this.n; i++) {
            for (int j = 0; j < this.n; j++) {
                StdOut.print(site[i][j] + " ");
            }
            StdOut.printf("%n");
        }
        StdOut.printf("%n");
    }
}