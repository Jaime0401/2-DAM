package com.tutorialspoint;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainApp {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");
		HelloWorld obj = (HelloWorld) context.getBean("HelloWorld");
		obj.getMessage();

		GoodByeWorld obj2 = (GoodByeWorld) context.getBean("GoodByeWorld");
		obj2.getMessage();
	}
}
