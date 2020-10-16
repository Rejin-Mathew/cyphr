import random
import time
while True:
    print("Game List")
    #time.sleep(1)
    print("1.Word guesser")
    #time.sleep(1)
    print("2.Number guesser")
    #time.sleep(1)
    print("3.Trivia")
    #time.sleep(1)
    print("4.Exit")
    #time.sleep(1)
    opt = int(input("Choose which game you wanna play!!!!!"))

    if opt == 2:
        print("Welcome to Number Guessor Game...............")
        time.sleep(1)
        hey = True
        while hey:
            print("Difficulty level")
            print("1.Hard")
            time.sleep(1)
            print("2.Medium")
            time.sleep(1)
            print("3.Easy")
            time.sleep(1)
            print("4.Exit")
            level = int(input("choose the difficulty level"))
            if level == 1:
                print("ATTENTION.................")
                time.sleep(1)
                print("you have 3 chances to guess the number correctly.if you guess that correctly then you win otherwise you lose.... ")
                time.sleep(1)
                print("Hint: The number is in between 1 and 50 ")
                time.sleep(3)
                random_high_no=random.randint(1,50)
                for i in range(0,3):
                    print("enter the number")
                    guess_no=int(input())
                    if guess_no>random_high_no:
                        print("number is greater")
                    elif guess_no<random_high_no:
                        print("number is lesser")
                    elif guess_no==random_high_no:
                        print("congrats the guessed number "+str(guess_no)+" is correct")
                        break
                if random_high_no!=guess_no:
                    print("you're chances are over better luck next time..the number was "+str(random_high_no))
                    break

            elif level == 2:
                print("ATTENTION.................")
                time.sleep(1)
                print("you have 3 chances to guess the number correctly.if you guess that correctly then you win otherwise you lose.... ")
                time.sleep(1)
                print("Hint: The number is in between 1 and 30 ")
                time.sleep(3)
                random_medium_no=random.randint(1,30)
                for i in range(0,3):
                    print("enter the number")
                    guess_no=int(input())
                    if guess_no>random_medium_no:
                        print("number is greater")
                    elif guess_no<random_medium_no:
                        print("number is lesser")
                    elif guess_no==random_medium_no:
                        print("congrats the guessed number "+str(guess_no)+" is correct")
                        break
                if random_medium_no!=guess_no:
                    print("you're chances are over better luck next time..the number was "+str(random_medium_no))
                    break
                break
            elif level == 3:
                print("ATTENTION.................")
                time.sleep(1)
                print("you have 3 chances to guess the number correctly.if you guess that correctly then you win otherwise you lose.... ")
                time.sleep(1)
                print("Hint: The number is in between 1 and 10 ")
                time.sleep(3)
                random_no=random.randint(1,10)
                for i in range(0,3):
                    print("enter the number")
                    guess_no=int(input())
                    if guess_no>random_no:
                        print("number is greater")
                    elif guess_no<random_no:
                        print("number is lesser")
                    elif guess_no==random_no:
                        print("congrats the guessed number "+str(guess_no)+" is correct")
                        break
                if random_no!=guess_no:
                    print("you're chances are over better luck next time..the number was "+str(random_no))
                    break
                break
            else:
                break
    elif opt==1:
        print("Welcome to Word Guessor Game........")
        time.sleep(1)
        print("Difficulty level")
        time.sleep(1)
        print("1.Hard")
        time.sleep(1)
        print("2.Medium")
        time.sleep(1)
        print("3.Easy")
        time.sleep(1)
        print("4.Exit")
        secondlevel = int(input("choose the difficulty level"))
        if secondlevel == 1:
            print("ATTENTION.................")
            time.sleep(1)
            print("you have 3 chances to guess the word correctly.if you guess that correctly then you win otherwise you lose.... ")
            time.sleep(1)
            print("Hint: Only the below mentioned words are used ")
            time.sleep(3)

            word_hard_list = ['lemon','orange','rejin','jincy','anoop','gokul','fathima','computer','cyphr red','cyphr blue','mustang','aventador','hacker','coder','heart','love','hate','cry','phone','car','bike','ship','aeroplane','language','laptop','mouse','keyboard','cpu','money','anonymous']
            for i in range(len(word_hard_list)):
                print(word_hard_list[i])
                random_word_select = random.randint(1,30)
                random_word = word_hard_list[random_word_select]
                for i in range(0,3):
                    print("enter the word")
                    guess_word= input()
                    if guess_word == random_word:
                        print("Hurray....you're guess is correct...good job...you won")
                    else:
                        print("try again...don't give up")
                if guess_word != random_word:
                    print("Better luck next time...you lose")
                    print("the correct anser is",random_word)
        elif secondlevel == 2:
            print("ATTENTION.................")
            time.sleep(1)
            print("you have 3 chances to guess the word correctly.if you guess that correctly then you win otherwise you lose.... ")
            time.sleep(1)
            print("Hint: Only the below mentioned words are used ")
            time.sleep(3)

            word_medium_list = ['computer','cyphr red','cyphr blue','mustang','aventador','hacker','coder','heart','love','hate','cry','phone','car','bike','aeroplane','language','laptop','mouse','keyboard','anonymous']
            for i in range(len(word_medium_list)):
                print(word_medium_list[i])
                random_word_select = random.randint(1,20)
                random_word = word_medium_list[random_word_select]
                for i in range(0,3):
                    print("enter the word")
                    guess_word= input()
                    if guess_word == random_word:
                        print("Hurray....you're guess is correct...good job...you won")
                    else:
                        print("try again...don't give up")
                if guess_word != random_word:
                    print("Better luck next time...you lose")
                    print("the correct anser is",random_word)
        elif secondlevel == 3:
            print("ATTENTION.................")
            time.sleep(1)
            print("you have 3 chances to guess the word correctly.if you guess that correctly then you win otherwise you lose.... ")
            time.sleep(1)
            print("Hint: Only the below mentioned words are used ")
            time.sleep(3)

            word_easy_list = ['mustang','aventador','hacker','coder','heart','love','keyboard','cpu','money','anonymous']
            for i in range(len(word_easy_list)):
                print(word_easy_list[i])
                random_word_select = random.randint(1,10)
                random_word = word_easy_list[random_word_select]
                for i in range(0,3):
                    print("enter the word")
                    guess_word= input()
                    if guess_word == random_word:
                        print("Hurray....you're guess is correct...good job...you won")
                    else:
                        print("try again...don't give up")
                        if guess_word != random_word:
                            print("Better luck next time...you lose")
                            print("the correct answer is",random_word)
        elif secondlevel == 4:
            break

    elif opt == 3:

        art_qus = ["Q. Lai Haraoba is a ritualistic festival observed in - \n 1) Nagaland\n 2) Tripura \n 3) Sikkim \n 4) Assam","Q. Kuchipudi is a dance form in India which originated in the State of - \n 1) Andhra Pradesh\n 2) Maharashtra\n 3) Gujarat\n 4) Kerala","Q. The author of the book titled The Daughter from a Wishing Tree : Unusual Tales about Women in Mythology is - \n 1) Sunita Namjoshi\n 2) Sarojini Sahoo\n 3) Shashi Deshpande\n 4) Shudha Murty","Q. Trade and Cultural Fare the Balijatra Festival is held every year in the Indian State of - \n 1) Chhattisgarh\n 2) Goa\n 3) Jharkhand\n 4) Odisha","Q. A for-day 'Shirul Lily' festival featuring the beautiful, flower, a unique species of ground fly is held in the Indian State of - \n 1) Manipur\n 2) Sikkim\n 3) Mizoram\n 4) Meghalaya","Q. The movie 'Gully Boy' has been nominated for the Oscar. The movie is directed by - \n 1) Raj Kumar Hirani\n 2) Sanjay Leela Bhansali\n 3) Prakash Goyal\n 4) Zoya Akhtar","Q. Lessons Life Taught Me, Unknowingly is an autobiography by which of the following? \n 1) Salman Rushdie\n 2) Anupam Kher\n 3) Shahid Afridi\n 4) Aamir Khan","Q. Who is the author of the book A Gallery of Rascals? \n 1) Arundhati Roy\n 2) Ruskin Bond\n 3) Vikram Seth\n 4) Toni Morrison","Q. Who wrote the book, India for Indians?\n 1) C. R. Das\n 2) M. G. Ranade\n 3) V. D. Savarkar\n 4) S. N. Banerjee","Q. Who is the author of the book India Shastra : Reflections on the Nation in our Time? \n 1) Narendra Modi\n 2) Shashi Tharoor\n 3) Manmohan Singh\n 4) A.P.J. Abdul Kalam","Q. Who was the author of the book Plagues and Peoples? \n 1) William H. McNeil\n 2) W.I. Thomas\n 3) Rachel Carson\n 4) David Cannadine","Q. Kathakali is a popular dance form prevalent in which state?\n 1) Andhra Pradesh\n 2) Karnataka\n 3) Tamil Nadu\n 4) Kerala","Q. Who is the author credited with composing the classical Tamil epic Silappatikaram? \n 1) Agastya\n 2) Ilango Adigal\n 3) Chithalai Chathanar\n 4) Tholkapiyyar","Q. Who started his career as a music composer in films as Sharmaji of the duo Sharmaji-Varmaji?\n 1) Khayyam\n 2) Naushad\n 3) Roshan\n 4) Jaidev","Q. The Coalition Years is the autobiography of - \n 1) Mr. Lalkrishna Advani\n 2) Mrs. Sonia Gandhi\n 3) Dr. Manmohan Singh\n 4) Mr. Pranav Mukharji","Q. The Kitab-ul-Hind is written in -\n 1) Urdu Language\n 2) Persian Language\n 3) Arabic Language\n 4) Turkish Language","Q. Chatkora dance is the folk dance of which tribe of Madhya Pradesh - \n 1) Bhil\n 2) Korku\n 3) Saharia\n 4) Gond","Q. Which script is used to write Haryanvi language? \n 1) Sanskrit\n 2) Hindi\n 3) Devanagari\n 4) None of the above","Q. Who was the author of the book History of British India? \n 1) Charles Grant\n 2) John Stuart Mill\n 3) James Mill\n 4) William Jones","Q. Who wrote the book, Desher Katha? \n 1) Sakharam Ganesh Deuskar\n 2) Rajendra Prasad\n 3) Nivaran Chandra\n 4) Murali Mohan Prasad","Q. Who is the author of the book Indira Gandhi : A Life in Nature? \n 1) Jai Ram Ramesh\n 2) M. Veerappa Moily\n 3) D.G. Tendulkar\n 4) Kiren Rijiju","Q. In which town of Uttar Pradesh would one find the 11 storid Pagal Baba Temple? \n 1) Vrindavan\n 2) Varanasi\n 3) Sarnath\n 4) Chitrakoot","Q. Bishwa Ijtema is held every year in -\n 1) India\n 2) Bangladesh\n 3) Indonesia\n 4) Maldives","Q. In which division of Chhattisgarh sings the 'Hulaki pata'?\n 1) Sarguja\n 2) Bastar\n 3) Bilaspur\n 4) Raipur","Q. What is Chhattisgarhi idioms for 'Sukh ke din aana'? \n 1) Din bahurana\n 2) Din purana\n 3) Din nandana\n 4) Din dekhana","Q. What is the traditional work of the Agaria tribe? \n 1) Iron craft\n 2) Wood craft\n 3) Tattoo craft\n 4) Bamboo craft","Q. Which of the following Indian film-makers was given the title of 'Ambassador' of Interlaken' in 2011 at Switzerland? \n 1) Yash Johar\n 2) Raj Kapoor\n 3) Subhash Ghai\n 4) Yash Chopra","Q. Dashain' is the grandest festival of .......... \n 1) Bangladesh\n 2) Bhutan\n 3) Sri Lanka\n 4) Nepal","Q. The art piece In Memoriam was a creation of which one of the following European painters? \n 1) Thomas Jones Barker\n 2) Joseph Noel Paton\n 3) Thomas Daniell\n 4) Charles D' Oyly","Q. Who among the following was awarded The Hindu Prize in Fiction category for the year 2018? \n 1) Neelum Saran Gour\n 2) N. Kalyan Raman\n 3) Manoranjan Byapari\n 4) Arunav Sinha","Q. The author of recently published book The Kiss of Life is - \n 1) Jessica Johnston\n 2) Anjali Sareen\n 3) Emraan Hashmi\n 4) Kartar Lalwan","Q. Which one of the following is not a folk dance of the Bundelkhand Region of UP? \n 1) Ravala dance\n 2) Dandia dance\n 3) Barhaiya dance\n 4) Raai dance","Q. Lathmar Holi is celebrated in - \n 1) Vrindavan\n 2) Barsana\n 3) Mathura\n 4) Gokul","Q. The prevalent term for Alpana, a folk art of Uttarakhand, is - \n 1) Aipan\n 2) Rangoli\n 3) Thapa\n 4) Jyunti","Q. Sun temple is situated in which of the following states? \n 1) Odisha\n 2) Gujarat\n 3) Karnataka\n 4) Tamil Nadu","Q. Which is post-harvest folk dance in Assam? \n 1) Ankia Nat\n 2) Bihu\n 3) Raut Nacha\n 4) Namgen","Q. Which one of the following publishers founded the Bharatiya Jnanpith trust to give the Jnanpith award to Indian writers? \n 1) The Times of India Group\n 2) The Hindustan Times Group\n 3) The Hindu Group\n 4) The Indian Express Group","Q. Kalchakra ceremony is associated with which of the following religions? \n 1) Hinduism\n 2) Buddhism\n 3) Jainism\n 4) Islam"]
        art_ans = [2,1,4,4,1,4,2,2,1,2,1,4,2,1,4,3,2,3,3,1,1,2,1,2,2,1,1,4,4,2,1,3,2,2,1,1,2,1]
        sports_qus = [ "Q. The Frank Worrell Trophy is a test-match (cricket) series played between Australia and -\n 1) West Indies\n 2) South Africa\n 3) New Zealand\n 4) England","Q. Who amongst the following has become the first in women cricket, to have 20 years of international cricket experience?\n 1) Smriti Mandhana\n 2) Ekta Bisht\n 3) Mithali Raj\n 4) Veda Krishnamurthy","Q. Ekaterina Paltceva and Manju Rani both are associated with the sport of - \n 1) Badminton\n 2) Basketball\n 3) Baseball\n 4) Boxing","Q. The Green Park Stadium, which hosted the 500th International test cricket match played by India in 2016, is situated in the Indian city of -\n1) Kanpur\n 2) Indore\n 3) Gwalior\n 4) Rajkot","Q. The Asian Amateur Boxing Championships' 2019 was held in - \n 1) Delhi, India\n 2) Moscow, Russia\n 3) Bangkok, Thailand\n 4) Nur-Sultan, Kazakhstan","Q. The headquarters of The International Olympic Committee is situated in - \n 1) Vienna, Austria\n 2) Lausanne, Switzerland\n 3) Geneva, Switzerland\n 4) Madrid, Spain","Q. Former Olympic Champion, 28 year old Li Xuerul who announced (in October 2019) her retirement, was associated with - \n 1) Baseball\n 2) Boxing\n 3) Softball\n4) Badminton","Q. Ben Stokes is associated with the game of - \n 1) Badminton\n 2) Football\n 3) Hockey\n 4) Cricket","Q. The Subroto Game is associated with the game of - \n 1) Hockey\n 2) Football\n 3) Cricket\n 4) Tennis","Q. Salwa Eid Nasser has won the gold medal in the 400 m women's race for 2019 IAAF World Athletics Championships. She is from which country? \n 1) Kenya\n 2) Kuwait\n 3) Peru\n 4) Bahrain","Q. IAAF World Athletics Championships 2019 was held at which place? \n 1) Ulan Ude, Russia\n 2) Doha, Qatar\n 3) Riyadh, UAE\n 4) Seoul, South Korea","Q. Sarah Taylor is a womn cricketer. She plays for which of the following countries? \n 1) Australia\n 2) New Zealand\n 3) South Africa\n 4) England","Q. Who is the second fastest batsman to score 25 centuries in the test format after Sir Don Bradman? \n 1) Virat Kohli\n 2) Mahela Jayawardene\n 3) Kane Williamson\n 4) Steve Smith","Q. The world's largest cricket stadium situated at - \n 1) Kolkata\n 2) Manchester\n 3) Melbourne\n 4) Motera","Q. Which of the following club has won the FIFA Club World Cup,2019? \n 1) Barcelona\n 2) Real Madrid\n 3) Juventas\n 4) Liverpool","Q. Where was India's first Day-Night Test organised? \n 1) Delhi\n 2) Kolkata\n 3) Mumbai\n 4) Chennai","Q. Which country hosted the the 13th South Asian Games 2019? \n 1) Bangladesh\n 2) Nepal\n 3) Bhutan\n 4) India","Q. Who among the following won the gold medal in 10,000 meters race in Asian Athletics Championship, 2017? \n 1) Govindan Lakshmanan\n 2) Adilet Kyshtabekov\n 3) Gopi Thonakal\n 4) Chen Chich","Q. Which of the following city hosted the 2017 Asian Athletics Championship? \n 1) Delhi\n 2) Bengaluru\n 3) Bhubaneshwar\n 4) Chandigarh","Q. What was the mascots for the 2017 FIFA Under-17 World Cup Football Tournament played in India? \n 1) SHERA\n 2) BHOLU\n 3) KHELEO\n 4) APPU","Q. Which among the following country won the Women's Rugby World Cup held in 2017? \n 1) England\n 2) New Zealand\n 3) Canada\n 4) Australia","Q. Which of the following teams won the final in Vijay Hazare Trophy 2018? \n 1) Rajasthan\n 2) Mumbai\n 3) Delhi\n 4) Punjab","Q. Who is the present captain of India's men National field hockey team?\n 1) Akashdeep Singh\n 2) Harmanpreet Singh\n 3) Rupinder Pal Singh\n 4) Manpreet Singh","Q. Archery is the national game of -\n 1) Bhutan\n 2) Denmark\n 3) Sri Lanka\n 4) Switzerland","Q. Rani Rampal has won the World Games Athlete of the Year award for 2019. She is associated with which of the following sports? \n 1) Tennis\n 2) Badminton\n 3) Hockey\n 4) Cricket","Q. Who among the following has won Australian Open Men’s Singles title 2020? \n 1) Roger Federer\n 2) Novak Djokovic\n 3) Dominic Thiem\n 4) Rafael Nadal","Q. Who amon the following Cricketer has been chosen for ICC ODI Cricketer of the Year for 2019 - \n 1) Virat Kohli\n 2) Ben Stokes\n 3) Rohit Sharma\n 4) Deepak Chahar","Q. Who amon the following Cricketer has been chosen for ICC Best Cricketer of the Year 2019 - \n 1) Rohit Sharma (India)\n 2) Ben Stokes (England)\n 3) Pat Cummins (Australia)\n 4) Virat Kohli (India)","Q. Who became the first World Badminton Champion from India? \n 1) Saina Newal\n 2) P V Sindhu\n 3) Sania Mirza\n 4) K Srikant","Q. Who is the first Indian woman to win an individual Olympic medal? \n 1) Karnam Malleshwari\n 2) Sania Mirza\n 3) P V Sindhu\n 4) Saina Newal","Q. Ace Against Odds is the autobiography of - \n 1) P T Usha\n 2) Sania Mirza\n 3) Marry Kom\n 4) Hima Das","Q. Fed Ex Cup and Augusta Masters are coveted trophies of the game of - \n 1) Squash\n 2) Golf\n 3) Billiards\n 4) Hockey","Q. Which team emerged Champion of the Vijay Hazare Trophy, 2019? \n 1) Tamil Nadu\n 2) Karnataka\n 3) Maharashtra\n 4) Delhi","Q. Where was the 17th IAAF World Athletics Championship, 2019 organised? \n 1) Dubai, Saudi Arabia\n 2) Alhasa, Saudi Arabia\n 3) Doha, Qatar\n 4) Tokyo, Japan","Q. Who won the silver medal in badmintion in the Asian Games, 2018? \n 1) Taipeis Tai Tzuying\n 2) Saina Nehwal\n 3) Syed Modi\n 4) P. V. Sindhu","Q. Which Indian batsman was the first to hit six consecutive sixes in first-class cricket? \n 1) Ravi Shastri\n 2) Sunil Gavaskar\n 3) Virat Kohli\n 4) Sachin Tendulkar","Q. The term Dolphin Kick is associated with which sport? \n 1) Football\n 2) Rugby\n 3) Swimming\n 4) Cricket","Q. Which Indian badminton player was runner-up at the 2019 Swiss Open tournament? \n 1) Kidambi Srikanth\n 2) Chetan Anand\n 3) Sai Praneeth\n 4) Parupalli Kashyap","Q. 'Triples' is a new format of - \n 1) Boxing\n 2) Judo\n 3) Chess\n 4) Badminton","Q. Who among the following won the Italian Open Women's Tennis Singles Title 2019? \n 1) Karolina Pliskova\n 2) Johanna Konta\n 3) Naomi Osaka\n 4) Serena Williams","Q. The National Dope Testing Laboratory functions under - \n 1) Ministry of Health and Family Welfare\n 2) Ministry of Science and Technology\n 3) Ministry of Youth Affairs and Sports\n 4) Ministry of Home Affairs","Q. Which one of the following is the motto of NCC? \n 1) Unity and Discipline\n 2) Unity and Integrity\n 3) Unity and Command\n 4) Unity and Service","Q. Indian shuttler P. V. Sindhu has become world champion in 2019 in badminton by defeating - \n 1) Japan's Nozomi Okuharan\n 2) Japan's Mayu Matsumoto\n 3) Japan's Akane Yamaguchi\n 4) Japan's TAI Tzu Ying","Q. ........ has become the first bowler in the world to claim five international hat-tricks? \n 1) Lasith Malinga (Sri Lanka)\n 2) Jasprit Bumrah (India)\n 3) Waseem Akaram (Pakistan)\n 4) Shane Warne (Australia)","Q. Who was the captain of the Indian Women's Hockey team that won the Asia Cup in November 2017? \n 1) Rani Rampal\n 2) Navjot Kaur\n 3) Savita Poonia\n 4) Deep Grace","Q. Who won the Women Single's title in the U.S. Opens Tennis Tournament, 2018? \n 1) Serena Williams\n 2) Anastasija Sevastova\n 3) Naomi Osaka\n 4) Elena Vesnia","Q. The World Cup Hockey tournament which was organized in Nov. 2018 in which of the following cities of India? \n 1) New Delhi\n 2) Bhubaneshwar\n 3) Puri\n 4) Kolkata","Q. Which Bangladesh all-rounder was the first and only cricketer to score a century and claim a hat-trick in the same test match? \n 1) Mashrafe Mortaza\n 2) Sohag Gazi\n 3) Shakib Al Hasan\n 4) Khaled Mahmud","Q. Who among the following has won the FIFA Player of the Year 2019? \n 1) Virgil van Dijk\n 2) Cristiano Ronaldo\n 3) Lionel Messi\n 4) Neymar","Q. When was the first sports policy was declared by Madhya Pradesh Government? \n 1) 1983\n 2) 1989\n 3) 1985\n 4) 1990" ]
        sports_ans = [1,3,4,1,3,2,4,4,2,4,2,4,4,4,4,2,2,1,3,3,2,2,4,1,3,2,3,2,2,1,2,2,2,3,4,1,3,3,4,1,3,1,1,1,1,3,2,2,3,2]
        tech_qus = ["Q. India's first satellite of 2020 GSAT-30 was successfully launched is a - \n 1) Remote Sensing Satellite\n 2) Communication Satelite\n 3) Spy Satellite\n 4) Metrological Satellite","Q. Very Large Array (VLA), a radio astronomy observatory which led to the recent discovery of smallest galaxies known to host massive black holes, is located in - \n 1) Paris\n 2) Hawaii Island\n 3) New York\n 4) Central New Mexico","Q. The study of images of deities falls within a branch of art history called - \n 1) Pictography\n 2) Lithography\n 3) Icthyography\n 4) Iconography","Q. Earth Imaging Satellite Goafen-10 has been launched onboard' Long March 4C rocket by - \n 1) Russia\n 2) China\n 3) Israel\n 4) Japan","Q. NEON the artificial human is claimed to have been developed by - \n 1) STAR Labs of Samsung\n 2) Apple Inc\n 3) Microsoft Corporation\n 4) Adobe Inc","Q. Name the project recently initiated by ISRO to safeguard Indian space assets from debris and other harm. \n 1) Project NETRA\n 2) Project DRISHTI\n 3) Project ROSHNI\n 4) Project Space","Q. Peter Higgs from United Kingdom and Francois Englert from Belgium had shared the 2013 Nobel Prize in which subject? \n 1) Chemistry\n 2) Medicine\n 3) Literature\n 4) Physics","Q. The 2019 Nobel Prize in Chemistry is awarded to Akira Yoshino, M. Stanley Whittingham and John B. Goodenough for which of the following works? \n 1) For the direct evolution of enzymes\n 2) For the phage display of peptides and antibodies\n 3) For the optical tweezers and their application to biological systems\n 4) For the development of lithium-ion batteries","Q. The International Atomic Energy Agency (IAEA) is an international organization that seeks to promote the peaceful uses of nuclear energy and to inhibit its use for any military purpose, including nuclear weapons. Where is the headquarters of IAEA? \n 1) Paris, France\n 2) New York, USA\n 3) New Delhi, India\n 4) Vienna, Austria","Q. Which of the following countries has opened the largest solar farm in Southeast Asia? \n 1) Vietnam\n 2) People's Republic of China\n 3) Myanmar\n 4) India","Q. UNESCO inaugurated the celebration of 2019 as the International Year of the Periodic Table of Chemical Elements to celebrate its completion of how many years? \n 1) 100\n 2) 150\n 3) 75\n 4) 50","Q. Recently, ISRO and CNES signed an agreement to set up a joint maritime surveillance system CNES is a space agency of which country? \n 1) Russia\n 2) Germany\n 3) France\n 4) Canada","Q. The book, The Origin of Species was written by - \n 1) Linnaeus\n 2) Lamarck\n 3) Mendel\n 4) Darwin","Q. The study of bones is done under the branch of science called - \n 1) geology\n 2) serology\n 3) orology\n 4) osteology","Q. A new frog species named Polypedates Bengalensis has been found in residential areas of - \n 1) Badu, North 24 Pargana district\n 2) Khordana-hala, South 24 Pargana district\n 3) Malda Town\n 4) Both (A) and (B)","Q. A new species of signal fish named Pteropsaron indicum has been discovered in -\n 1) The Ganges near Sahibganj\n 2) Deep waters of the Laksha-dweep Sea off Kerala Coast\n 3) Andaman Island coast\n 4) Kochi harbour","Q. Which satellite is dedicated as India's first multi wavelength space observatory? \n 1) Astrosat\n 2) SARAL\n 3) SRMSAT\n 4) Jugnu","Q. Which of the following is a commonly used chemical method for purifying water? \n 1) Hibernation\n 2) Excavation\n 3) Chlorination\n 4) Denitrification","Q. Which of the following is a part of the process involved in water cycle? \n 1) Evaporation\n 2) Sublimation\n 3) Freezing\n 4) Meltin","Q. Name the nuclear-capable surface-to-surface intercontinental ballistic missile developed by the Defence Research and Development Organisation (DRDO)? \n 1) Prithvi III\n 2) Trishul\n 3) Agni 5\n 4) Barak-8","Q. What is the application of the GSAT-31 satellite launched by India on 6 February, 2019? \n 1) Earth observation\n 2) Navigation\n 3) Climate and Environment\n 4) Communication","Q. With which foreign country India has collaborated to develop the supersonic cruise missile called BrahMos? \n 1) France\n 2) China\n 3) Japan\n 4) Russia","Q. Which space agency has created history in October 2019 by sending 'all women' astronauts into the space walk? \n 1) Roscosmos (Russia)\n 2) NASA (USA)\n 3) ISRO (India)\n 4) CNSA (China)","Q. Which of the following is India's first indigenously developed vaccine? \n 1) BCG\n 2) Rotavac\n 3) DPT\n 4) Inject able Polio vaccine","Q. A geostationary satellite is positioned at a distance of how many kilometers above mean sea level? \n 1) 35, 880\n 2) 37, 800\n 3) 35, 786\n 4) 32, 000","Q. What is the name of the new dwarf planet which was discovered in 2005? \n 1) Eris\n 2) Erin\n 3) Eros\n 4) Eric","Q. Which of the following company designed the world's first 30-KW class ATHENA drone destroying laser? \n 1) Boeing\n 2) Thales\n 3) Lockheed Martin\n 4) Raytheon","Q. The Nobel Prize for Physics in 2018 was awarded for pioneering work in which field? \n 1) Laser Physics\n 2) Quantum Mechanics\n 3) Thermodynamics\n 4) Aerodynamics","Q. The name of scientist who designed India's first space satellite Aryabhatta is - \n 1) Prof. U. R. Rao\n 2) Prof. Yashpal\n 3) Prof. C. N. R. Rao\n 4) Dr. A. S. Kiran Kumar","Q. Which of the following statements is not true about the optical fibres? \n 1) They provide longer number of connectivity for telephones\n 2) They are less noisy\n 3) They are cheaper\n 4) They have longer life-time","Q. Who was first Indian director of the Indian Institute of Science, Bangalore? \n 1) Dorabji Tata\n 2) C V Raman\n 3) Homi Jehangir Bhabha\n 4) Satish Dhawan"]
        tech_ans = [2,4,4,2,1,1,4,4,4,1,2,3,4,4,4,2,1,3,1,3,4,4,2,2,3,1,3,1,1,3,2]
        gk_qus = ["Q. Which city in the USA is referred to as the City of Golden Gate? \n 1) Florida\n 2) San Fransisco\n 3) Los Angeles\n 4) New York","Q. 49th Parallel is a boundary line between - \n 1) Brazil and Argentina\n 2) Germany and France\n 3) USA and Canada\n 4) Norway and Finland","Q. Khanatm, Pakhupila, and Cherokan are famous folk dances of -1) Mizoram2) Manipur3) Meghalaya4) Arunachal Pradesh","Q. How many players are there in a team of Volleyball? \n 1) 5\n 2) 6\n 3) 7\n 4) 8","Q. Deodhar Trophy is a prestigious tournament of - \n 1) Football\n 2) Cricket\n 3) Hockey\n 4) Badminton","Q. Which team emerge champion of the FIFA under-17 Football World Cup, 2019? \n 1) Argentina\n 2) Germany\n 3) Brazil\n 4) Spain","Q. FIH Men's Hockey World Cup, 2023 will be hosted in India in - \n 1) Kolkata\n 2) Jalandhar\n 3) Chandigarh\n 4) Bhubaneswar and Rourkela","Q. Beighton Cup is the prestigious championship of the game of -\n 1) Cricket\n 2) Basket Ball\n 3) Hockey\n 4) Football","Q. Fruit cracking disease in Pomegranate is caused due to the deficiency of - \n 1) Zinc\n 2) Iron\n 3) Boron\n 4) Sulphar","Q. National Environmental Engineering Research Institute is located in - \n 1) Nagpur\n 2) Pune\n 3) Chandigarh\n 4) Kolkata","Q. Who was the Governor General of British India at the time of Simon Commission and Nehru Report? \n 1) Lord Rippon\n 2) Lord Kornowalis\n 3) Lord Irwin\n 4) Lord Mountbatten","Q. Where was the first-ever Global Refugee Forum organised in 2019? \n 1) Newyork\n 2) Geneva\n 3) Berlin\n 4) Barcelona","Q. Vembanand lake is located in - \n 1) Karnataka\n 2) Kerala\n 3) Andhra Pradesh\n 4) Tamil Nadu","Q. Bara-La and Shipki-La passes are located in - \n 1) Uttarakhand\n 2) Sikkim\n 3) Arunachal Pradesh\n 4) Himachal Pradesh","Q. Who called Mahatma Gandhi as Mahatma for the first time? \n 1) Jawaharlal Nehru\n 2) Rabindranath Tagore\n 3) Netaji Subhash Chandra Bose\n 4) Sardar Vallabh Bhai Patel","Q. Who founded the Indian Independence League at California? \n 1) Madan Lal Dhingra\n 2) Shyamji Krishna Varma\n 3) Tarak Nath Das\n 4) Surendra Nath Bandyopadhyay","Q. Which greatest leader of the Indian national movement wrote History of the Indian National Congress? \n 1) Motilal Nehru\n 2) Sarojini Naidu\n 3) Pattabhi Sitaramayya\n 4) J B Kripalani","Q. Who has been named Time Person of the Year 2019? \n 1) Greta Thunberg\n 2) Malala Yousafzai\n 3) Donald Trump\n 4) Vladimir Putin","Q. What is India's rank on the WEF's Global Gender Gap Report, 2020? \n 1) 109th\n 2) 110th\n 3) 112th\n 4) 113th","Q. What is India's rank on the UNDP's Human Development Index, 2019? \n 1) 129th\n 2) 128th\n 3) 127th\n 4) 126th","Q. Nautanki, Raslila, Kajri, Chappeli, Jaita are popular folk dances of - \n 1) Haryana\n 2) Jharkhand\n 3) Uttar Pradesh\n 4) Bihar","Q. Barabati Stadium is located in - \n 1) Cuttack\n 2) Ranchi\n 3) Bhubaneshwar\n 4) Patna","Q. International Girl Child Day is observed on - \n 1) October 11\n 2) September 11\n 3) October 20\n 4) October 15","Q. Naomi Osaka and Simona Halep are eminent sports women associated with the game of - \n 1) Badminton\n 2) Lawn Tennis\n 3) Table Tennis\n 4) Women Cricket","Q. Which country hosted the 13th South Asian Games, 2019? \n 1) Bangladesh\n 2) Nepal\n 3) India\n 4) Bhutan","Q. Centre for Ecological Science is located in - n 1) Mumbai\n 2) Bengaluru\n 3) Hyderabad\n 4) Pune","Q. Suprabha and Surbhi are varieties of - \n 1) Ginger\n 2) Brinjal\n 3) Sugarcane\n 4) Chilli","Q. Where is the headquarters of the Insurance Regulatory and Development Authority (IRDA)? \n 1) New Delhi\n 2) Hyderabad\n 3) Mumbai\n 4) Bangalore","Q. Betla National Park is located in - \n 1) Bihar\n 2) Odisha\n 3) Assam\n 4) Jharkhand","Q. Ballon d'Or honour is associated with the game of - \n 1) Basket Ball\n 2) Football\n 3) Polo\n 4) Tennis","Q. Gugamal National Park is located in - \n 1) Assam\n 2) Karnataka\n 3) Maharashtra\n 4) Madhya Pradesh","Q. Mauritius and Poovan are varieties of - \n 1) Brinjal\n 2) Ginger\n 3) Chilli\n 4) Banana","Q. Dwarfness in sugarcane is caused by -\n 1) Virus\n 2) Bacteria\n 3) Insect\n 4) Fungus","Q. Raniganj coal mines are located in - \n 1) Jharkhand\n 2) Bihar\n 3) Odisha\n 4) West Bengal","Q. Who is the writer of a famous travelogue Rihla in Arabic? \n 1) Ibn Battuta\n 2) Al Biruni\n 3) Megasthenis\n 4) Dara Shikoh","Q. Which freedom fighter edited The Dawn of India and Dainik Basumati? \n 1) Barindra Kumar Ghosh\n 2) Aurobindo Ghosh\n 3) Bipin Chandra Pal\n 4) Rammohan Roy","Q. Which Constitutional amendment was also referred to as the Mini Constitution of India? \n 1) 40th amendment\n 2) 41st amendment\n 3) 42nd amendment\n 4) 43rd amendment","Q. Which country operationalized world's largest radio telescope? \n 1) USA\n 2) China\n 3) Russia\n 4) India","Q. Katerina Sakellaropoulou was elected the first woman President of - \n 1) Greece\n 2) Spain\n 3) Finland\n 4) Netherland","Q. India's first satellite of 2020 GSAT-30 was successfully launched is a - \n 1) Remote Sensing Satellite\n 2) Communication Satelite\n 3) Spy Satellite\n 4) Metrological Satellite"]
        gk_ans = [2,3,1,2,2,3,4,3,3,1,3,2,2,4,2,3,3,1,3,1,3,1,1,2,2,2,1,2,4,2,3,4,1,4,1,1,3,2,1,2]
        science_qus = ["Q. What is the bond order of CO group? \n 1) 1\n 2) 2.5\n 3) 3.5\n 4) 3","Q. Natural rubber is a polymer of - \n 1) Isoprene\n 2) Styrene\n 3) Vinyl Acetate\n 4) Propene","Q. Oxygen is absent in - \n 1) Kerosene\n 2) Glass\n 3) Soil\n 4) Cement","Q. The main component of greenhouse gases is -\n 1) carbon dioxide\n 2) methane\n 3) nitrous oxide\n 4) None of the above/ More than one of the above","Q. The pH value of water is - \n 1) 4\n 2) 7\n 3) 12\n 4) 18","Q. The by-product of photosynthesis is - \n 1) CO2\n 2) O2\n 3) energy\n 4) sugar","Q. Solar energy is converted into ATP in - \n 1) mitochondria\n 2) chloroplast\n 3) ribosome\n 4) peroxisome","Q. The actual location or place where an organism lives is called - \n 1) habitat\n 2) ecosystem\n 3) niche\n 4) biome","Q. The interaction between algae and fungi to form lichen is called - \n 1) parasitism\n 2) mutualism\n 3) commensalism\n 4) conversion","Q. Body temperature is regulated by -\n 1) medulla\n 2) thalamus\n 3) hypothalamus\n 4) cerebellum","Q. The unit of electric power is - \n 1) ampere\n 2) volt\n 3) coulomb\n 4) watt","Q. The device to measure electric current is - \n 1) voltmeter\n 2) ammeter\n 3) voltameter\n 4) Potentiometer","Q. What is measured in Hertz? \n 1) Frequency\n 2) Energy\n 3) Heat\n 4) Quality","Q. Sound wave in air is - \n 1) transverse\n 2) longitudinal\n 3) electromagnetic\n 4) polarized","Q. Which one of the following quantities does not have unit? \n 1) Stress\n 2) Force\n 3) Strain\n 4) Pressure","Q. Which of the following is not a type of element? \n 1) Metals\n 2) Nonmetals\n 3) Gases\n 4) Metalloids","Q. Which of the following is also known as laughing gas? \n 1) Nitric oxide\n 2) Nitrous oxide\n 3) Nitrogen pentoxide\n 4) Nitrogen","Q. The number of electrons and neutrons in an element is 18 and 20 respectively. Its mass number is \n  -1) 22\n 2) 2\n 3) 38\n 4) 20","Q. Who is regarded as the Father of Modern Chemistry? \n 1) Rutherford\n 2) Einstein\n 3) Lavoisier\n 4) C. V. Raman","Q. Limestone, chalk and marble are different forms of - \n 1) Sodium hydroxide\n 2) Ammonium hydroxide\n 3) Calcium hydroxide\n 4) Calcium carbonate","Q. AIDS is caused by - \n 1) Helminth\n 2) Bacteria\n 3) Fungus\n 4) Virus","Q. Which of the following hormones contains iodine? \n 1) Testosterone\n 2) Adrenaline\n 3) Thyroxine\n 4) Insulin","Q. In which organ of the human body are the lymphocytes formed? \n 1) Liver\n 2) Bone marrow\n 3) Spleen\n 4) Pancreas","Q. Which of the following does not have any enzyme in its cells? \n 1) Lichen\n 2) Virus\n 3) Bacteria\n 4) Algae","Q. Which is the longest muscle in the human body? \n 1) Gracilis\n 2) Soleus\n 3) Sartorius\n 4) Trapezius","Q. Which one of the following is a scalar quantity? \n 1) Force\n 2) Pressure\n 3) Velocity\n 4) Acceleration","Q. The sunlight from the sun to the earth reaches in - \n 1) 5 minutes\n 2) 6 minutes\n 3) 8 minutes\n 4) 10 minutes","Q. The unit of pressure is - \n 1) kg/ cm2\n 2) kg/ cm\n 3) kg/ mm\n 4) None of the above/ More than one of the above","Q. An ammeter has ........... resistance, so that it passes maximum current through it. \n 1) Infinite\n 2) Very less\n 3) Very high\n 4) High","Q. Which of the following is equal to Hertz? \n 1) s-1\n 2) m s-2\n 3) s\n 4) m / s","Q. Which nutrient provides the maximum energy on breakdown? \n 1) Fibres\n 2) Proteins\n 3) Fats\n 4) Carbohydrates","Q. Which organ in the human body helps to maintain balance? \n 1) Heart\n 2) Liver\n 3) Ear\n 4) Brain","Q. Which disease is prevented with the help of Salk's vaccine?\n 1) Measles\n 2) Polio\n 3) Chicken pox\n 4) Small pox","Q. Sodium metal is stored in - \n 1) Kerosene\n 2) Ether\n 3) Water\n 4) Acetone","Q. The process of movement of molecules from a higher concentration place to a lower concentration places is known as : \n 1) Condensation\n 2) Evaporation\n 3) Diffusion\n 4)Sublimation","Q. K-shell is the .......... energy level. \n 1) Third\n 2) Fourth\n 3) First\n 4) Second"]
        science_ans = [4,1,1,4,2,2,2,1,2,3,4,2,1,2,3,3,2,3,3,4,4,3,2,2,3,2,3,4,2,1,3,3,2,1,3,3]
        ar = []
        ar_jack = []
        ar_jones = []
        arr_jack = []
        arr_jones = []
        ar_happy = []
        arr_happy = []
        ar_hugo = []
        arr_hugo = []
        ar_player = []
        arr_player = []
        print("Welcome to the world of Trivia.......")
        #time.sleep(1)

        print("Number of players!!!!!!!")
        #time.sleep(1)
        print("1.Two")
        #time.sleep(1)
        print("2.Three")
        #time.sleep(1)
        print("3.Four")
        #time.sleep(1)
        print("4.Play with Bot")
        #time.sleep(1)
        print("5.Exit")
        #time.sleep(1)
        num = int(input("Enter the number of players"))
        print("ATTENTION..............")
        #time.sleep(1)
        print("The questions are from  5 Topics")
        #time.sleep(1)
        print("* Art")
        #time.sleep(1)
        print("* Sports")
        #time.sleep(1)
        print("* Technology")
        #time.sleep(1)
        print("* General knowledge")
        #time.sleep(1)
        print("* Science")
        #time.sleep(1)

        if num == 1:
            print("The first players name is Jack and second players name is Jones")
            time.sleep(2)
            for i in range(5):#qus loop
                if i == 0:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 37)#number of total qus in list
                    print(hey)
                    print(art_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    print(ar_jack)
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print(arr_jack)
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 37)
                    print(hello)
                    print(art_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                elif i ==1:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 49)#number of total qus in list
                    print(hey)
                    print(sports_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    print(ar_jack)
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print(arr_jack)
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 49)
                    print(hello)
                    print(sports_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                elif i ==2:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 30)#number of total qus in list
                    print(hey)
                    print(tech_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 30)
                    print(hello)
                    print(tech_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                elif i == 3:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 39)#number of total qus in list
                    print(hey)
                    print(gk_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 39)
                    print(hello)
                    print(gk_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                elif i == 4:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 35)#number of total qus in list
                    print(hey)
                    print(science_qus[hey])
                    ar_jack.append(hey)#passing the correct ans position
                    print(ar_jack)
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print(arr_jack)
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 35)
                    print(hello)
                    print(science_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
            #for i in range(5):
            i = 0
            while i<=4:
                count_jack = 0
                count_jones = 0
                if i == 0:
                    ans_checkj = art_ans[ar_jack[i]]
                    ans_checkjo = art_ans[ar_jones[i]]

                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)
                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    i = i+1
                    #else:
                    #    pass
                if i == 1:
                    ans_checkj = sports_ans[ar_jack[i]]
                    ans_checkjo = sports_ans[ar_jones[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)
                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    #else:
                        #pass
                    i = i+1
                if i == 2:
                    ans_checkj = tech_ans[ar_jack[i]]
                    ans_checkjo = tech_ans[ar_jones[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)
                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    #else:
                        #pass
                    i = i+1
                if i == 3:
                    ans_checkj = gk_ans[ar_jack[i]]
                    ans_checkjo = gk_ans[ar_jones[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)
                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    #else:
                        #pass
                    i = i+1
                if i == 4:
                    ans_checkj = science_ans[ar_jack[i]]
                    ans_checkjo = science_ans[ar_jones[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)
                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    #else:
                        #pass
                    i = i+1

            print("SCOREBOARD")
            print("1.Jack :",count_jack)
            print("2.Jones:",count_jones)
            if count_jack>count_jones:
                print("Congrats......Jack you won the game..Good work")
            elif count_jones>count_jack:
                print("Congrats......Jones you won the game..Good work")
            else:
                print("Tough Game....its a draw Congrats to Jack and Jones")

        if num == 2:
            print("The first players name is Jack and second players name is Jones and third players name is Happy")
            time.sleep(2)
            for i in range(5):#qus loop
                if i == 0:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 37)#number of total qus in list
                    print(hey)
                    print(art_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    print(ar_jack)
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print(arr_jack)
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 37)
                    print(hello)
                    print(art_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                    print("Question for Happy!!!!!!")
                    hell = random.randint(0, 37)
                    print(art_qus[hell])
                    ar_happy.append(hell)
                    ans_happy = int(input())
                    arr_happy.append(ans_happy)
                elif i ==1:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 49)#number of total qus in list
                    print(hey)
                    print(sports_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    print(ar_jack)
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print(arr_jack)
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 49)
                    print(hello)
                    print(sports_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                    print("Question for Happy!!!!!!")
                    hell = random.randint(0, 49)
                    print(sports_qus[hell])
                    ar_happy.append(hell)
                    ans_happy = int(input())
                    arr_happy.append(ans_happy)
                elif i ==2:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 30)#number of total qus in list
                    print(hey)
                    print(tech_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 30)
                    print(hello)
                    print(tech_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                    print("Question for Happy!!!!!!")
                    hell = random.randint(0, 30)
                    print(tech_qus[hell])
                    ar_happy.append(hell)
                    ans_happy = int(input())
                    arr_happy.append(ans_happy)
                elif i == 3:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 39)#number of total qus in list
                    print(hey)
                    print(gk_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 39)
                    print(hello)
                    print(gk_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                    print("Question for Happy!!!!!!")
                    hell = random.randint(0, 39)
                    print(gk_qus[hell])
                    ar_happy.append(hell)
                    ans_happy = int(input())
                    arr_happy.append(ans_happy)
                elif i == 4:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 35)#number of total qus in list
                    print(hey)
                    print(science_qus[hey])
                    ar_jack.append(hey)#passing the correct ans position
                    print(ar_jack)
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print(arr_jack)
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 35)
                    print(hello)
                    print(science_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                    print("Question for Happy!!!!!!")
                    hell = random.randint(0, 35)
                    print(science_qus[hell])
                    ar_happy.append(hell)
                    ans_happy = int(input())
                    arr_happy.append(ans_happy)
                    #for i in range(5):
            i = 0
            count_jack = 0
            count_jones = 0
            count_happy = 0
            while i<=4:
                #print("check")
                if i == 0:
                    ans_checkj = art_ans[ar_jack[i]]
                    ans_checkjo = art_ans[ar_jones[i]]
                    ans_checkh = art_ans[ar_happy[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack = count_jack + int(1)
                        print(count_jack)
                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    if ans_checkh == arr_happy[i]:
                        count_happy += int(1)
                    i = i+1
                            #else:
                                #pass
                if i == 1:
                    ans_checkj = sports_ans[ar_jack[i]]
                    ans_checkjo = sports_ans[ar_jones[i]]
                    ans_checkh = sports_ans[ar_happy[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)
                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    if ans_checkh == arr_happy[i]:
                        count_happy += int(1)
                    i = i+1
                            #else:
                                #pass
                if i == 2:
                    ans_checkj = tech_ans[ar_jack[i]]
                    ans_checkjo = tech_ans[ar_jones[i]]
                    ans_checkh = tech_ans[ar_happy[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)

                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    if ans_checkh == arr_happy[i]:
                        count_happy += int(1)
                    i = i+1
                            #else:
                                #pass
                if i == 3:
                    ans_checkj = gk_ans[ar_jack[i]]
                    ans_checkjo = gk_ans[ar_jones[i]]
                    ans_checkh = gk_ans[ar_happy[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)

                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    if ans_checkh == arr_happy[i]:
                        count_happy += int(1)
                    i = i+1
                            #else:
                                #pass
                if i == 4:
                    ans_checkj = science_ans[ar_jack[i]]
                    ans_checkjo = science_ans[ar_jones[i]]
                    ans_checkh = science_ans[ar_happy[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)
                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    if ans_checkh == arr_happy[i]:
                        count_happy += int(1)
                    i = i + 1

            print("SCOREBOARD")
            print("1.Jack :",count_jack)
            print("2.Jones:",count_jones)
            print("3.Happy:",count_happy)
            if count_jack > count_jones and count_jack>count_happy:#if count_jack>count_happy
                print("Congrats......Jack you won the game..Good work")
            elif count_jones>count_jack and count_jones>count_happy:#if count_jones>count_happy:
                print("Congrats......Jones you won the game..Good work")
            elif count_happy>count_jack and count_happy>count_jones:#if count_happy>count_jones:
                print("Congrats......Happy you won the game..Good work")
            elif count_jack == count_jones and count_jack == count_happy:
                print("Impossible....you guys are really challenging each other....its a draw for all")
            elif count_jack == count_jones:
                print("Tough Game....its a draw Congrats to Jack and Jones")
            elif count_jack == count_happy:
                print("Tough Game....its a draw Congrats to Jack and Happy")
            elif count_happy == count_jones:
                print("Tough Game....its a draw Congrats to Happy and Jones")
        if num == 3:
            print("The first players name is Jack and second players name is Jones and third players name is Happy and fourth players name is Hugo")
            time.sleep(2)
            for i in range(5):#qus loop
                if i == 0:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 37)#number of total qus in list
                    print(hey)
                    print(art_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    print(ar_jack)
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print(arr_jack)
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 37)
                    print(hello)
                    print(art_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                    print("Question for Happy!!!!!!")
                    hell = random.randint(0, 37)
                    print(art_qus[hell])
                    ar_happy.append(hell)
                    ans_happy = int(input())
                    arr_happy.append(ans_happy)
                    print("Question for Hugo!!!!!!")
                    hug = random.randint(0, 37)
                    print(art_qus[hug])
                    ar_hugo.append(hug)
                    ans_hugo = int(input())
                    arr_hugo.append(ans_hugo)
                elif i ==1:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 49)#number of total qus in list
                    print(hey)
                    print(sports_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    print(ar_jack)
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print(arr_jack)
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 49)
                    print(hello)
                    print(sports_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                    print("Question for Happy!!!!!!")
                    hell = random.randint(0, 49)
                    print(sports_qus[hell])
                    ar_happy.append(hell)
                    ans_happy = int(input())
                    arr_happy.append(ans_happy)
                    print("Question for Hugo!!!!!!")
                    hug = random.randint(0, 49)
                    print(sports_qus[hug])
                    ar_hugo.append(hug)
                    ans_hugo = int(input())
                    arr_hugo.append(ans_hugo)
                elif i ==2:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 30)#number of total qus in list
                    print(hey)
                    print(tech_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 30)
                    print(hello)
                    print(tech_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                    print("Question for Happy!!!!!!")
                    hell = random.randint(0, 30)
                    print(tech_qus[hell])
                    ar_happy.append(hell)
                    ans_happy = int(input())
                    arr_happy.append(ans_happy)
                    print("Question for Hugo!!!!!!")
                    hug = random.randint(0, 30)
                    print(tech_qus[hug])
                    ar_hugo.append(hug)
                    ans_hugo = int(input())
                    arr_hugo.append(ans_hugo)
                elif i == 3:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 39)#number of total qus in list
                    print(hey)
                    print(gk_qus[hey])
                    ar_jack.append(hey) #passing the correct ans position
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 39)
                    print(hello)
                    print(gk_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                    print("Question for Happy!!!!!!")
                    hell = random.randint(0, 39)
                    print(gk_qus[hell])
                    ar_happy.append(hell)
                    ans_happy = int(input())
                    arr_happy.append(ans_happy)
                    print("Question for Hugo!!!!!!")
                    hug = random.randint(0, 39)
                    print(gk_qus[hug])
                    ar_hugo.append(hug)
                    ans_hugo = int(input())
                    arr_hugo.append(ans_hugo)
                elif i == 4:
                    print("Question for Jack!!!!!!!")
                    #time.sleep(1)
                    hey = random.randint(0, 35)#number of total qus in list
                    print(hey)
                    print(science_qus[hey])
                    ar_jack.append(hey)#passing the correct ans position
                    print(ar_jack)
                    ans_jack = int(input())
                    arr_jack.append(ans_jack) #passing the answer by jack
                    print(arr_jack)
                    print("Question for Jones!!!!!!")
                    hello = random.randint(0, 35)
                    print(hello)
                    print(science_qus[hello])
                    ar_jones.append(hello)
                    ans_jones = int(input())
                    arr_jones.append(ans_jones)
                    print("Question for Happy!!!!!!")
                    hell = random.randint(0, 35)
                    print(science_qus[hell])
                    ar_happy.append(hell)
                    ans_happy = int(input())
                    arr_happy.append(ans_happy)
                    print("Question for Hugo!!!!!!")
                    hug = random.randint(0, 35)
                    print(science_qus[hug])
                    ar_hugo.append(hug)
                    ans_hugo = int(input())
                    arr_hugo.append(ans_hugo)
            i = 0
            count_jack = 0
            count_jones = 0
            count_happy = 0
            count_hugo = 0
            while i<=4:
                if i == 0:
                    ans_checkj = art_ans[ar_jack[i]]
                    ans_checkjo = art_ans[ar_jones[i]]
                    ans_checkh = art_ans[ar_happy[i]]
                    ans_checkhu = art_ans[ar_happy[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack = count_jack + int(1)
                        print(count_jack)
                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    if ans_checkh == arr_happy[i]:
                        count_happy += int(1)
                    if ans_checkhu == arr_hugo[i]:
                        count_hugo += int(1)
                    i = i+1


                        #else:
                            #pass

                if i == 1:
                    ans_checkj = sports_ans[ar_jack[i]]
                    ans_checkjo = sports_ans[ar_jones[i]]
                    ans_checkh = sports_ans[ar_happy[i]]
                    ans_checkhu = sports_ans[ar_happy[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)
                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    if ans_checkh == arr_happy[i]:
                        count_happy += int(1)
                    if ans_checkhu == arr_hugo[i]:
                        count_hugo += int(1)
                    i = i+1

                        #else:
                            #pass
                if i == 2:
                    ans_checkj = tech_ans[ar_jack[i]]
                    ans_checkjo = tech_ans[ar_jones[i]]
                    ans_checkh = tech_ans[ar_happy[i]]
                    ans_checkhu = tech_ans[ar_happy[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)

                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    if ans_checkh == arr_happy[i]:
                        count_happy += int(1)
                    if ans_checkhu == arr_hugo[i]:
                        count_hugo += int(1)
                    i = i+1

                        #else:
                            #pass
                if i == 3:
                    ans_checkj = gk_ans[ar_jack[i]]
                    ans_checkjo = gk_ans[ar_jones[i]]
                    ans_checkh = gk_ans[ar_happy[i]]
                    ans_checkhu = gk_ans[ar_happy[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)

                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    if ans_checkh == arr_happy[i]:
                        count_happy += int(1)
                    if ans_checkhu == arr_hugo[i]:
                        count_hugo += int(1)
                    i = i+1

                        #else:
                            #pass
                if i == 4:
                    ans_checkj = science_ans[ar_jack[i]]
                    ans_checkjo = science_ans[ar_jones[i]]
                    ans_checkh = science_ans[ar_happy[i]]
                    ans_checkhu = science_ans[ar_happy[i]]
                    if ans_checkj == arr_jack[i]:
                        count_jack += int(1)
                        print(count_jack)
                    if ans_checkjo == arr_jones[i]:
                        count_jones += int(1)
                    if ans_checkh == arr_happy[i]:
                        count_happy += int(1)
                    if ans_checkhu == arr_hugo[i]:
                        count_hugo += int(1)
                    i = i + 1

                        #else:
                            #pass

            print("SCOREBOARD")
            print("1.Jack :",count_jack)
            print("2.Jones:",count_jones)
            print("3.Happy:",count_happy)
            print("4.Hugo:",count_hugo)
            if count_jack > count_jones and count_jack>count_happy and count_jack>count_hugo :#if count_jack>count_happy
                print("Congrats......Jack you won the game..Good work")
            elif count_jones>count_jack and count_jones>count_happy and count_jones>count_hugo:#if count_jones>count_happy:
                print("Congrats......Jones you won the game..Good work")
            elif count_happy>count_jack and count_happy>count_jones and count_happy> count_hugo:#if count_happy>count_jones:
                print("Congrats......Happy you won the game..Good work")
            elif count_hugo>count_jack and count_hugo>count_jones and count_hugo>count_happy:
                print("Congrats......Hugo you won the game..Good work")
            elif count_jack == count_jones:
                print("Tough Game....its a draw Congrats to Jack and Jones")
            elif count_jack == count_happy:
                print("Tough Game....its a draw Congrats to Jack and Happy")
            elif count_jack == count_hugo:
                print("Tough Game....its a draw Congrats to Jack and Hugo")
            elif count_happy == count_jones:
                print("Tough Game....its a draw Congrats to Happy and Jones")
            elif count_hugo == count_jones:
                print("Tough Game....its a draw Congrats to Hugo and Jones")
            elif count_happy == count_hugo:
                print("Tough Game....its a draw Congrats to Happy and Hugo")
            elif count_jack == count_jones and count_jack == count_happy:
                print("Tough Game....its a draw Congrats to Happy and Jack and Jones")
            elif count_jack == count_jones and count_jack == count_hugo:
                print("Tough Game....its a draw Congrats to Hugo and Jack and Jones")
            elif count_happy == count_jones and count_happy == count_hugo:
                    ("Tough Game....its a draw Congrats to Hugo and Happy and Jones")
            elif count_jack == count_hugo and count_jack == count_happy:
                print("Tough Game....its a draw Congrats to Happy and Jack and Hugo")
            else:
                print("Impossible....you guys are really challenging each other....its a draw for all")
        elif num == 4:
            print("Difficulty Level")
            print("1.Hard")
            print("2.Medium")
            print("3.Easy")
            dif = int(input())
            if dif == 1:
                bot_point = 4
                for i in range(5):#qus loop
                    if i == 0:
                        print("Question for the Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 37)#number of total qus in list
                        #print(hey)
                        print(art_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        print(ar_player)
                        ans_player = int(input())
                        arr_player.append(ans_player) #passing the answer by jack
                        print(arr_player)
                    elif i ==1:
                        print("Question for the Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 49)#number of total qus in list
                        print(play)
                        print(sports_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        print(ar_player)
                        ans_player = int(input())
                        arr_player.append(ans_player) #passing the answer by jack
                        print(arr_player)
                    elif i ==2:
                        print("Question for Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 30)#number of total qus in list
                        print(play)
                        print(tech_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        ans_player = int(input())
                        arr_player.append(ans_player)
                        print(arr_player)
                    elif i == 3:
                        print("Question for Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 39)#number of total qus in list
                        print(play)
                        print(gk_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        ans_player = int(input())
                        arr_player.append(ans_player)
                        print(arr_player)
                    elif i == 4:
                        print("Question for Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 35)#number of total qus in list
                        print(play)
                        print(science_qus[play])
                        ar_player.append(play)#passing the correct ans position
                        print(ar_player)
                        ans_player = int(input())
                        arr_player.append(ans_player) #passing the answer by jack
                        print(arr_player)
                i = 0
                while i<=4:
                    count_player = 0
                    if i == 0:
                        ans_checkp = art_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)
                        i = i+1
                        #else:
                        #    pass
                    if i == 1:
                        ans_checkp = sports_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)

                        #else:
                            #pass
                        i = i+1
                    if i == 2:
                        ans_checkp = tech_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)
                        #else:
                            #pass
                        i = i+1
                    if i == 3:
                        ans_checkp = gk_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)

                        #else:
                            #pass
                        i = i+1
                    if i == 4:
                        ans_checkp = science_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)
                        #else:
                            #pass
                        i = i+1

                print("SCOREBOARD")
                print("1.Player :",count_player)
                print("2.Bot:",bot_point)
                if count_player>bot_point:
                    print("Congrats......Player you won the game..Good work")
                elif bot_point>count_player:
                    print("You lose....Bot win the game")
                else:
                    print("Tough Game....its a draw")
            if dif == 2:
                bot_point = 3
                for i in range(5):#qus loop
                    if i == 0:
                        print("Question for the Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 37)#number of total qus in list
                        #print(hey)
                        print(art_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        print(ar_player)
                        ans_player = int(input())
                        arr_player.append(ans_player) #passing the answer by jack
                        print(arr_player)
                    elif i ==1:
                        print("Question for the Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 49)#number of total qus in list
                        print(play)
                        print(sports_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        print(ar_player)
                        ans_player = int(input())
                        arr_player.append(ans_player) #passing the answer by jack
                        print(arr_player)
                    elif i ==2:
                        print("Question for Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 30)#number of total qus in list
                        print(play)
                        print(tech_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        ans_player = int(input())
                        arr_player.append(ans_player)
                        print(arr_player)
                    elif i == 3:
                        print("Question for Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 39)#number of total qus in list
                        print(play)
                        print(gk_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        ans_player = int(input())
                        arr_player.append(ans_player)
                        print(arr_player)
                    elif i == 4:
                        print("Question for Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 35)#number of total qus in list
                        print(play)
                        print(science_qus[play])
                        ar_player.append(play)#passing the correct ans position
                        print(ar_player)
                        ans_player = int(input())
                        arr_player.append(ans_player) #passing the answer by jack
                        print(arr_player)
                i = 0
                while i<=4:
                    count_player = 0
                    if i == 0:
                        ans_checkp = art_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)
                        i = i+1
                        #else:
                        #    pass
                    if i == 1:
                        ans_checkp = sports_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)

                        #else:
                            #pass
                        i = i+1
                    if i == 2:
                        ans_checkp = tech_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)
                        #else:
                            #pass
                        i = i+1
                    if i == 3:
                        ans_checkp = gk_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)

                        #else:
                            #pass
                        i = i+1
                    if i == 4:
                        ans_checkp = science_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)
                        #else:
                            #pass
                        i = i+1

                print("SCOREBOARD")
                print("1.Player :",count_player)
                print("2.Bot:",bot_point)
                if count_player>bot_point:
                    print("Congrats......Player you won the game..Good work")
                elif bot_point>count_player:
                    print("You lose....Bot win the game")
                else:
                    print("Tough Game....its a draw")
            if dif == 3:
                bot_point = 2
                for i in range(5):#qus loop
                    if i == 0:
                        print("Question for the Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 37)#number of total qus in list
                        #print(hey)
                        print(art_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        print(ar_player)
                        ans_player = int(input())
                        arr_player.append(ans_player) #passing the answer by jack
                        print(arr_player)
                    elif i ==1:
                        print("Question for the Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 49)#number of total qus in list
                        print(play)
                        print(sports_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        print(ar_player)
                        ans_player = int(input())
                        arr_player.append(ans_player) #passing the answer by jack
                        print(arr_player)
                    elif i ==2:
                        print("Question for Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 30)#number of total qus in list
                        print(play)
                        print(tech_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        ans_player = int(input())
                        arr_player.append(ans_player)
                        print(arr_player)
                    elif i == 3:
                        print("Question for Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 39)#number of total qus in list
                        print(play)
                        print(gk_qus[play])
                        ar_player.append(play) #passing the correct ans position
                        ans_player = int(input())
                        arr_player.append(ans_player)
                        print(arr_player)
                    elif i == 4:
                        print("Question for Player!!!!!!!")
                        #time.sleep(1)
                        play = random.randint(0, 35)#number of total qus in list
                        print(play)
                        print(science_qus[play])
                        ar_player.append(play)#passing the correct ans position
                        print(ar_player)
                        ans_player = int(input())
                        arr_player.append(ans_player) #passing the answer by jack
                        print(arr_player)
                i = 0
                while i<=4:
                    count_player = 0
                    if i == 0:
                        ans_checkp = art_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)
                        i = i+1
                        #else:
                        #    pass
                    if i == 1:
                        ans_checkp = sports_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)

                        #else:
                            #pass
                        i = i+1
                    if i == 2:
                        ans_checkp = tech_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)
                        #else:
                            #pass
                        i = i+1
                    if i == 3:
                        ans_checkp = gk_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)

                        #else:
                            #pass
                        i = i+1
                    if i == 4:
                        ans_checkp = science_ans[ar_player[i]]

                        if ans_checkp == arr_player[i]:
                            count_player += int(1)
                            print(count_player)
                        #else:
                            #pass
                        i = i+1

                print("SCOREBOARD")
                print("1.Player :",count_player)
                print("2.Bot:",bot_point)
                if count_player>bot_point:
                    print("Congrats......Player you won the game..Good work")
                elif bot_point>count_player:
                    print("You lose....Bot win the game")
                else:
                    print("Tough Game....its a draw")
        elif num == 5:
            break

    elif opt==4:
        exit()
