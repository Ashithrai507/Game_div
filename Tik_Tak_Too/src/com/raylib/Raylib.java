package com.raylib;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.concurrent.CountDownLatch;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

/**
 * Minimal Swing-based implementation of the tiny Raylib API used by the sample UI.
 * It opens a real window and draws the last text requested each frame. This is
 * purely for local development without the native raylib dependency.
 */
public class Raylib {
    public static final int RAYWHITE = 0xFFFFFFFF;
    public static final int BLACK = 0x000000FF;

    private final int width;
    private final int height;
    private final String title;

    private volatile boolean shouldClose = false;
    private RenderPanel panel;
    private JFrame frame;

    public Raylib(int width, int height, String title) {
        this.width = width;
        this.height = height;
        this.title = title;

        CountDownLatch latch = new CountDownLatch(1);
        final JFrame[] fRef = new JFrame[1];

        // Create GUI on EDT and wait until ready
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame(title);
            f.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
            f.setSize(width, height);
            f.setLocationRelativeTo(null);
            panel = new RenderPanel();
            f.add(panel);
            f.addWindowListener(new WindowAdapter() {
                @Override
                public void windowClosing(WindowEvent e) {
                    shouldClose = true;
                }

                @Override
                public void windowClosed(WindowEvent e) {
                    shouldClose = true;
                }
            });
            f.setVisible(true);
            fRef[0] = f;
            latch.countDown();
        });

        try {
            latch.await();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        // retrieve frame and panel references created on EDT
        frame = fRef[0];
        // panel was assigned inside invokeLater; to keep typesafe we read it from the frame content
        panel = (RenderPanel) frame.getContentPane().getComponent(0);

        System.out.printf("[Raylib] Opened window %dx%d: %s%n", width, height, title);
    }

    public boolean windowShouldClose() {
        return shouldClose;
    }

    public void beginDrawing() {
        // no-op for Swing; prepare if needed
    }

    public void clearBackground(int color) {
        panel.setBackgroundInt(color);
    }

    public void drawText(String text, int x, int y, int fontSize, int color) {
        panel.setText(text, x, y, fontSize, color);
    }

    public void endDrawing() {
        panel.repaint();
        try {
            Thread.sleep(16); // ~60 FPS cap and avoid busy-waiting
        } catch (InterruptedException ignored) {
            Thread.currentThread().interrupt();
        }
    }

    public void closeWindow() {
        SwingUtilities.invokeLater(() -> {
            if (frame != null) {
                frame.dispose();
            }
        });
    }

    // Inner panel that performs the actual drawing
    private static class RenderPanel extends JPanel {
        private static final long serialVersionUID = 1L;
        private String text = "";
        private int tx = 10, ty = 20, fontSize = 16;
        private Color bg = Color.WHITE;
        private Color fg = Color.BLACK;

        synchronized void setBackgroundInt(int color) {
            int r = (color >> 24) & 0xFF;
            int g = (color >> 16) & 0xFF;
            int b = (color >> 8) & 0xFF;
            this.bg = new Color(r, g, b);
        }

        synchronized void setText(String text, int x, int y, int fontSize, int color) {
            this.text = text;
            this.tx = x;
            this.ty = y;
            this.fontSize = fontSize;
            int r = (color >> 24) & 0xFF;
            int g = (color >> 16) & 0xFF;
            int b = (color >> 8) & 0xFF;
            this.fg = new Color(r, g, b);
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2 = (Graphics2D) g;
            g2.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
            // draw background
            synchronized (this) {
                g2.setColor(bg);
                g2.fillRect(0, 0, getWidth(), getHeight());
                g2.setColor(fg);
                g2.setFont(new Font("SansSerif", Font.PLAIN, fontSize));
                g2.drawString(text, tx, ty);
            }
        }
    }
}
