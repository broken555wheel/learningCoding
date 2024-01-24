import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.Color;
import java.awt.Dimension;

import javax.swing.ImageIcon;

public class SwingLesson {
	public static void main(String[] args) {
		MyLabel label = new MyLabel();
		MyFrame myFrame = new MyFrame(); // Instanciating the MyFrame class
		MyTextField myTextField = new MyTextField();
		myFrame.add(myTextField);
	}

}

class MyFrame extends JFrame {
	MyFrame() {
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setTitle("Frame title goes here"); //
		this.setResizable(false); // prevents resizing of our frame
		this.setSize(420, 420); // Sets the x and y dimensions of the frame
		ImageIcon logo = new ImageIcon("logo.jpg");
		this.setIconImage(logo.getImage());
		this.getContentPane().setBackground(Color.CYAN);
		this.setVisible(true); // makes the frame visible

	}

}

class MyLabel extends JLabel{
	MyLabel(){
		ImageIcon image = new ImageIcon("image.jpg");
		this.setIcon(image);
		this.setText("Bro, do you even code?");
		this.setHorizontalTextPosition(JLabel.LEFT);  //
	}
}

class MyTextField extends JTextField{
	MyTextField(){
		this.setPreferredSize(new Dimension(250,40));
	}
}

//class MyButton extends 