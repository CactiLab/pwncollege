# To-do list of PwnIoT.Cacti.academy

## Functionality

- [] (Deadline: ???, 2023; Elijah) Update the docker image to support Cortex-A, RISC-V (qemu-user), Cortex-M (qemu). All challenges regardless type will use the same image for now. 
- [] (Deadline: ???, 2023; Elijah) Install Z shell.
- [] (Deadline: ???, 2023; Dikshit) Make the website publicly accesible. 1. Get a public IP? 2. HTTPS certificate
- [] (Deadline: ???, 2022; Developer) Add a function to track user input. Step 1. record user's input to the challenge; Step 2. Store user input to a history database table (user, user input). Eventual goal is to design an automatic help and hinting system based on user input.
- [] (Deadline: ???, 2022; Developer) Design the defense-challenges database tables.
- [] (Deadline: ???, 2022; Developer) Design the create-challenges database tables.
- [] (Deadline: ???, 2022; Developer) Tutorials page: There should a tutorials page, where we can add documents, vedios, youtube links, slides etc.


## GUI

- [] (Deadline: ???, 2023; Elijah) Develop a theme: Check the pwn college website and their source code, we need to develop similar theme on our own.
- [] (Deadline: ???, 2023; Elijah) About: Create a credit page to list all of the contributors to the platform (names, pictures). The page should be easily updateable, if possible include admin access to update the credit page. Admin edit access from the platform will allow to update without modifying source code.
- [] (Deadline: ???, 2022; Developer) Statistics page: Modify the statistics page that will show CTF-Challenges, Defense Challenges, Create Challenges solved by a user.
- [] (Deadline: ???, 2022; Developer) Defense Challenges: Create a defense challenges page that will show all the defense challenges. This page will be similar to the CTF-Challenges page. It will include a flag capture test script and a functional requirement test provided by us, to check if the submitted solution maintains the functional requirements and if the bug is fixed. The provided Defense Challenges will capture a flag by default, but if the user fixes these bugs of the challenges it will not get the default flag. There should also be a way (scripts to automate submission compilation) for the user to interact with the platform to submit the challenges.
- [] (Deadline: ???, 2022; Developer) Create Challenges: Create Challenges page should give the users some kind of interaction method to design the challenges. After designing the challenge the users will submit it to the platform, our interaction method will update the challenge as CTF-Challenges or Defensive Challenges. The user who creates the challenge needs to solve the challenge first and submit an exploit on the platform. Lastly, there should be admin access to the submitted challenge source code and exploit to review those.
- [] (Deadline: ???, 2022; Developer) User discussion page:** Create a discussion page or discord server like pwn college where users can discuss about the challenges.
- [] (Deadline: ???, 2022; Developer) In-page discussion feature:
- [] (Deadline: ???, 2022; Developer) Update the README page. Remove pwn.collge stuff. Explain we forked from them.

## For the todo-list of Challenges. Please refer to https://github.com/CactiLab/CTF-challenges