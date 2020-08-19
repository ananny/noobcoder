import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.WindowConstants;
import javax.swing.JTextField;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.lang.*;
import java.io.*;


public class Calculator  extends JComponent implements ActionListener { 
        
       static String s = " ";
       static double num1 = 0;
       static double num2 = 0;
       static double result = 0;
       static JTextField t1;
       static JButton btn1;
       static JButton btn2;
       static JButton btn3;
       static JButton btn4;
       static JButton btn5;
       static JButton btn6;
       static JButton btn7;
       static JButton btn8;
       static JButton btn9;
       static JButton btn11;
        public static void main(String[] args) {                        
                        
                Calculator cal =  new Calculator(); 
                JFrame frame = new JFrame("CALCULATOR");                
                frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
                        frame.setLocation(700,200);
                        frame.setSize(700,600);                        
                   
                        frame.getContentPane();
                        //frame.setBackground(Color.GRAY);                        
                        frame.setLayout(null);                                             
                        t1 = new JTextField(10);
                        t1.setBounds(110,120,430,50);   
                 
                 
                       btn1 = new JButton("1");
                       btn1.setBounds(200,200,50,50);
                       btn1.setActionCommand("1");
                       btn1.addActionListener(cal);                       
                       frame.add(btn1);
                                                                
                        
                        btn2 = new JButton("2");  
                        btn2.setBounds(270,200,50,50);                      
                        btn2.setActionCommand("2");
                        btn2.addActionListener(cal);                
                        frame.add(btn2);
                        
                        
                        btn3 = new JButton("3");
                        btn3.setBounds(340,200,50,50);
                        btn3.setActionCommand("3");
                        btn3.addActionListener(cal);                
                        frame.add(btn3);
                       
                        
                        btn4 = new JButton("4");
                        btn4.setBounds(200,270,50,50);
                        btn4.setActionCommand("4");
                        btn4.addActionListener(cal);                
                        frame.add(btn4);
                       
                        
                        btn5 = new JButton("5");
                        btn5.setBounds(270,270,50,50);
                        btn5.setActionCommand("5");
                        btn5.addActionListener(cal);                
                        frame.add(btn5);
                       
                        
                        btn6 = new JButton("6");
                        btn6.setBounds(340,270,50,50);
                        btn6.setActionCommand("6");
                        btn6.addActionListener(cal);                
                        frame.add(btn6);
                       
                        
                        btn7 = new JButton("7");
                        btn7.setBounds(200,340,50,50);
                        btn7.setActionCommand("7");
                        btn7.addActionListener(cal);                
                        frame.add(btn7);
                       
                        
                        btn8 = new JButton("8");
                        btn8.setBounds(270,340,50,50);
                        btn8.setActionCommand("8");
                        btn8.addActionListener(cal);                
                        frame.add(btn8);
                       
                        
                        btn9 = new JButton("9");
                        btn9.setBounds(340,340,50,50);
                        btn9.setActionCommand("9");
                        btn9.addActionListener(cal);                
                        frame.add(btn9);
                        
                        
                        JButton btn10 = new JButton(".");
                        btn10.setBounds(200,410,50,50);
                        btn10.setActionCommand(".");
                        btn10.addActionListener(cal);                
                        frame.add(btn10);
                       
                        
                        btn11 = new JButton("0");
                        btn11.setBounds(270,410,50,50);
                        btn11.setActionCommand("0");
                        btn11.addActionListener(cal);                
                        frame.add(btn11);
                       
                        
                        JButton btn12 = new JButton("(");
                        btn12.setBounds(340,410,50,50);
                        btn12.setActionCommand("(");
                        btn12.addActionListener(cal);                
                        frame.add(btn12);
                       
                        
                        JButton btn13 = new JButton(")");
                         btn13.setBounds(410,410,50,50);
                        btn13.setActionCommand(")");
                        btn13.addActionListener(cal);                
                        frame.add(btn13);
                       
                        
                        JButton btn14 = new JButton("<-");
                         btn14.setBounds(410,200,115,50);
                        btn14.setActionCommand("<-");
                        btn14.addActionListener(cal);                
                        frame.add(btn14);
                       

                        JButton btn15 = new JButton("%");
                        btn15.setBounds(410,270,115,50);
                        btn15.setActionCommand("%");
                        btn15.addActionListener(cal);    
                        frame.add(btn15);
                       
                        
                        
                        JButton btn16 = new JButton("C");    
                        btn16.setBounds(410,340,115,50);             
                        btn16.setActionCommand("C");
                        btn16.addActionListener(cal);    
                        frame.add(btn16);
                        
                        
                        JButton btn17 = new JButton("=");
                        btn17.setBounds(478,410,50,50);      
                        btn17.setActionCommand("=");
                        btn17.addActionListener(cal);   
                        frame.add(btn17);
                        
                        JButton btn18 = new JButton("+");
                        btn18.setBounds(130,200,50,50);
                        btn18.setActionCommand("+");
                        btn18.addActionListener(cal);                
                        frame.add(btn18);            
                                                 
                        JButton btn19 = new JButton("-");
                        btn19.setBounds(130,270,50,50);
                        btn19.setActionCommand("-");
                        btn19.addActionListener(cal);                
                        frame.add(btn19);
                        
                        JButton btn20 = new JButton("x");
                        btn20.setBounds(130,340,50,50);
                        btn20.setActionCommand("*");
                        btn20.addActionListener(cal);                
                        frame.add(btn20);
                        
                        JButton btn21 = new JButton("/");
                        btn21.setBounds(130,410,50,50);
                        btn21.setActionCommand("/");
                        btn21.addActionListener(cal);                
                        frame.add(btn21);                        
                                                            
                        frame.add(t1);
                        frame.add(cal);
                        frame.setVisible(true);
                   
        }//Main()
        
         @Override
        public void actionPerformed(ActionEvent e) {
                String command = e.getActionCommand();
                if(command.equals("1")) {
                        String str = t1.getText() + btn1.getText();
                        t1.setText(str);
                }
                else if(command.equals("2")) {
                        String str = t1.getText() + btn2.getText();
                        t1.setText(str);
                }                
                else if(command.equals("3")) {
                        String str = t1.getText() + btn3.getText();
                        t1.setText(str);
                }
                else if(command.equals("4")) {
                        String str = t1.getText() + btn4.getText();
                        t1.setText(str);
                }
                else if(command.equals("5")) {
                         String str = t1.getText() + btn5.getText();
                        t1.setText(str);
                }
                else if(command.equals("6")) {
                        String str = t1.getText() + btn6.getText();
                        t1.setText(str);
                }
                else if(command.equals("7")) {
                        String str = t1.getText() + btn7.getText();
                        t1.setText(str);
                }
                else if(command.equals("8")) {
                         String str = t1.getText() + btn8.getText();
                        t1.setText(str);
                }
                else if(command.equals("9")) {
                         String str = t1.getText() + btn9.getText();
                        t1.setText(str);
                }
                else if(command.equals(".")) {
                        String str = t1.getText() + '.';
                        t1.setText(str);//btn010();
                }
                else if(command.equals("0")) {
                        String str = t1.getText() + btn11.getText();
                        t1.setText(str);
                }
                else if(command.equals("(")) {
                        String str = t1.getText() + '(';
                        t1.setText(str);                        
                }
                else if(command.equals(")")) {
                       String str = t1.getText() + ')';
                        t1.setText(str); 
                }
                else if(command.equals("<-")) {
                        String str = t1.getText();
                        StringBuffer sb = new StringBuffer(str);
                        sb.deleteCharAt(sb.length()-1);
                        String s1 = sb.toString();
                        t1.setText(s1);
                        //btn014();
                }
                else if(command.equals("%")) {
                        s = "%";
                        num1 = Integer.valueOf(t1.getText());
                        t1.setText(" ");                       
                }
                else if(command.equals("C")) {
                        num1 = 0;
                        num2 = 0;
                        s = " ";
                        result = 0;
                        String str = " ";
                        t1.setText(str); 
                }
                else if(command.equals("=")) {                      
                       num2 = Double.valueOf(t1.getText());
                       
                       if("+".equals(s)) {                              
                              result =  (num1 + num2);
                       }
                       else if("-".equals(s)) {
                                result = (num1 - num2);
                       }
                       else if("*".equals(s)) {
                                result =  (num1 * num2);
                       }
                       else if("/".equals(s)) {
                                result =  (num1 / num2);
                       }
                       else {
                                result =  (num1 % num2);
                       }     
                       String str = String.valueOf(result);         
                       t1.setText(str);                                            
                }                
                 else if(command.equals("+")) {
                        s = "+";
                        num1 = Integer.valueOf(t1.getText());
                        t1.setText(" ");
                }
                 else if(command.equals("-")) {
                        s = "-";
                        num1 = Integer.valueOf(t1.getText());
                        t1.setText(" ");
                }                
                 else if(command.equals("*")) {
                         s = "*";
                        num1 = Integer.valueOf(t1.getText());
                        t1.setText(" ");
                }
                else {
                        s = "/";
                        num1 = Integer.valueOf(t1.getText());//btn018();
                        t1.setText(" ");
                }  
     }//actionPerformed()       
}//class Calculator



        






