from PIL import Image, ImageDraw, ImageFont

  


def coupons(names: list, ws:list, date:list, certificate: str, font_path1: str,font_path2: str,font_path3: str):
   
    for name in names:
        for workshop in ws:
            for dates in date:
                text_y_position =775
                text_x_position=930
                text_z_position=1000
                # opens the image
                img = Image.open(certificate, mode ='r')
                  
                # gets the image width
                image_width = img.width
                  
                # gets the image height
                image_height = img.height 
           
                # creates a drawing canvas overlay 
                # on top of the image
                draw = ImageDraw.Draw(img)
           
                # gets the font object from the 
                # font file (TTF)
                font1 = ImageFont.truetype(
                    font_path1,
                    100 # change this according to your needs
                )
           
                # fetches the text width for 
                # calculations later on
                text_width, _ = draw.textsize(name, font = font1)
           
                draw.text(
                    (
                        # this calculation is done 
                        # to centre the image
                        (image_width - text_width) / 2,
                        text_y_position
                    ),
                    name,
                    font = font1 , fill="black"  )
                font2 = ImageFont.truetype(
                    font_path2,
                    35 # change this according to your needs
                )
                font3 = ImageFont.truetype(
                    font_path3,
                    35 # change this according to your needs
                )
           
                # fetches the text width for 
                # calculations later on
                text_width, _ = draw.textsize(workshop, font = font2)
           
                draw.text(
                   (
                       # this calculation is done 
                       # to centre the image
                       (image_width - text_width) / 2,
                       text_x_position
                   ),
                   workshop,
                   font = font2 , fill="black"  )
                draw.text(
                   (
                       # this calculation is done 
                       # to centre the image
                       (image_width - text_width) / 2,
                       text_z_position
                   ),
                   dates,
                   font = font2 , fill="black"  )
                # saves the image in png format
                r=name+dates
                img.save("{}.png".format(r)) 
        
   
   
        
      
             
      
# Driver Code
if __name__ == "__main__":
   
    # some example of names
    NAMES1 = ['Aditya Ghadge ',
             'Manpreet Kaur ',
             'Prabha Pamula ',
             'Rohan Bhamre ',
             'Sahil Madhyan ',
             'Aditya Sharma ',
             'Chaitanya Sondur ',
             'Hitakrit Goplani ',
             'Rahul Maurya ',
             'Sarthak Adhangale ',
             'Vaishnav Kondhalkar ',
             'Vedang Chavan ',
             'Bhavya Kurup ',
             'Nandana Nair ',
             'Omkar Mourya ',
             'Krish Mehta ']
    NAMES3=['Pratik R. Waghmode ', 
    'Sanskar R. Halpati ', 
    'Mihir Suhanda ',
    'Pankaj Ukirde ', 
    'Mansi Pawar ',
    'Madhura Ghanwat ',
    'Vrundali Patil ',
    'Pooja Narayanan ',
    'Gaurang Kedare ',
    'Omkar Maurya ', 
    'Aatharvaa Shiveshwarkar ',
    'Shreyash Dhasade ',
    'Vikas Dhakane ',
    'Shruti Patil ',
    'Shreya Kamble ',
    'Jheel Panchal ',
    'Gauri Kurmude ',
    'Prasad Gourshettiwar ',
    'Rahul Patil ',
    'Shikha Negi ',
    'Srishti Gharat ',
    'Harsh Falak ',
    'Ritiksha Mhatre ',
    'Aniruddha Mestry ',
    'Manisha Walunj ',
    'Krishna Shelar ', 
    'Yashasvi Singh ' ]
    NAMES2=['Kajal Ghusale ',
'Pankaj Ukirde ',
'Pradeesh Reddy ',
'Udit Koli ',
'Mihir Suhanda ',
'Manpreet Kaur ',
'Pooja Ghadge ',
'Nidhi Gharat ',
'Bhakti Sawashe ',
'Pooja Narayan ']
    NAMES4=[]
    NAMES5=[]
    NAMES6=['Sania Khan ']
    NAMES7=[]
    NAMES8=[]
    NAMES9=['Pooja Narayanan ',	
'Vikas Dhakane ',	
'Vedant Pawar ',
'Manish Mhatre ',
'Abhishek Kakad ',
'Yash Kurade '	,
'Prathmesh Bhingarde ',
'Hritika Mulay ',
'Atharva Godkar ',	
'Harshal Talreja ',
'Krishang Ukey ',	
'Vedika Chavan ',	
'Aditya Dange ',	
'Omkar Mourya ',	
'Pritam Dhamak ',
'Vineet Gupta ',	
'Aman Yadav ',
'Anish Godse ',	
'Prathamkumar Bumb ',	
'Rahul Singh ',	
'Aatharvaa Shiveshwarkar ',	
'Harshal Paymode ',	
'Bhavik Gondhali ',	
'Baltej Gill ',	
'Vivek Jambhulkar ',	
'Vedant Patil ']
    NAMES10=['Atharva Shinde ',
             'Yash Kurade ',
             'Rayyan Shaikh ',
             'Manish Mhatre ',
             'Atishkar Singh ',
             'Vedant Pawar ',
             'Kalpesh Rathod ',
             'Prakruti Rathod ',
             'Kasturi Bapat ',
             'Riya Parab ',
             'Prathamesh More ',
             'Prathamesh Bhingarde ',
             'Mayur Mistry ',
             'Yash Kadam ',
             'Sanjeev Nishad ',
             'Sumaiya Sayyed ',
             'Rahul Singh ',
             'Ratan Poojari ',
             'Omkar Upadhyay ',
             'Rutik Jaybhaye ',
             'Mrudula Gotmare ',
             'Tejas Dabholkar ',
             'Sanskriti Patil ',
             'Mitali Pagare ',
             'Swaraj Bangar ',
             'Sukanya Pingle ',
             'Suyog Bharsakle ',
             'Hitesh Gaonkar ',
             'Anushri Kadam ',
             'Atharva Chaudhari ',
             'Shardul Kadam ',
             'Kadambari Dalvi ',
             'Tejal.N ',
             'Sneha Bhalerao ',
             'Aadarsh Pandit ',
             'Harsh Gawali ',
             'Soham Malgundkar ',
             'Yash Chhaproo ',
             'Aniket Pradhan ',
             'Kartikey Shukla ',
             'Vikas Dhakane ',
             'Anuj Raina ',
             'Harsh Falak ',
             'Sohan Shetty ',
             'Shibha Negi ',
             'Krishna Shelar ']
    NAMES5=['Aditya Ayare ',
            'Aditya Naresh ',
            'Amaan Radhanpura ',
            'Anushka Darure ',
            'Ashutosh Deorukhkar ',
            'Atharva Dabhade ',
            'Brice Dsouza ',
            'Chaitali Kulkarni ',
            'Dhanshree Pandey ',
            'Disha Bhat ',
            'Gaurav Kulkarni ',
            'Jesica Bijju ',
            'Kaushik Kotian ',
            'Khwaish Shahani ',
            'Kunal Purswani ',
            'Manisha Walunj ',
            'Mehvish Khan ',
            'Nikita Kumavat ',
            'Prathamesh Jawale ',
            'Preeti Sonawane ',
            'Priyanka Amrute ',
            'Puja Mahankuda ',
            'Rahul Shukla ',
            'Roshan Bangera ',
            'Rujuta Bhor  ',
            'Shreya Kamble ',
            'Shruti Nikhare ',
            'Shruti Patil ',
            'Suja Ravindran ',
            'Sujal Sawdekar ',
            'Tejas Rokade ',
            'Vikas Dhakane ',
            'Pooja Narayan ',
            'Rahul Jeswani ',
            'Ritesh Tahilramani ',
            ]
    NAMES11=['Girish Gopalakrishnan ',
 'Akshay Jain ', 
 'Yukta Talagana ',
'Vinaya Nair ']
    
    str1='for participating in the workshop on '
    str2=' which was conducted from'
    str3=' which was conducted on'
    str4='for participating in '
    WS1=[str1+'"'+'Web App using Firebase'+'"'+str2]
    WS2=[str1+'"'+'New 8051 Embedded C Programming'+'"']
    WS3=[str1+'"'+'PCB Design'+'"'+str2]
    WS4=[str1+'"'+'3D Printing'+'"'+str2]
    WS5=[str1+'"'+'Three.js'+'"'+str2]
    WS9=[str1+'"'+'ESP32 and Micropython'+'"'+str2]
    WS10=[str4+'"'+'BE and Beyond'+'"'+str2]
    WS11=[str4+"'"+'Technovation - Project Exhibition Competition'+"'"]
    date1=['2nd to 3rd July, 2022.']
    date3=['3rd to 5th August, 2022.']
    date2=['which was conducted on 30th July, 6th August and 13th August, 2022.']
    date4=['25th to 26th August, 2022.']
    date5=['17th to 18th September, 2022.']
    date6=['24th September, 2022.']
    date7=['6th October, 2022.']
    date8=['29th to 30th December, 2022.']
    date9=['6th to 7th February, 2023.']
    date10=['23rd to 24th February, 2023.']
    date11=['which was conducted on 20th March 2023.']
    
  
  
      
    # path to font
    FONT1 = "C:/Users/SANIA/Downloads/Libre_Baskerville/LibreBaskerville-Italic.ttf"
    FONT2= "C:/Users/SANIA/Downloads/Lora/static/Lora-Regular.ttf"
    FONT3= 'C:/Users/SANIA/Downloads/Lora/static/Lora-Bold.ttf'
    
    
      
    # path to sample certificate
    CERTIFICATE = "C:/Users/SANIA/Downloads/Copy of isa certi.png"
   
coupons(NAMES1,WS1,date1,CERTIFICATE,FONT1,FONT2,FONT3)
coupons(NAMES3,WS3,date3,CERTIFICATE,FONT1,FONT2,FONT3)
coupons(NAMES2,WS2,date2,CERTIFICATE,FONT1,FONT2,FONT3)
coupons(NAMES11,WS11,date11,CERTIFICATE,FONT1,FONT2,FONT3)

coupons(NAMES9,WS9,date9,CERTIFICATE,FONT1,FONT2,FONT3)
coupons(NAMES10,WS10,date10,CERTIFICATE,FONT1,FONT2,FONT3)
coupons(NAMES5,WS5,date5,CERTIFICATE,FONT1,FONT2,FONT3)
