# To-do list of PwnIoT.Cacti.academy

## Meeting 9/11/2023

## Functionality

- [Wei] (Deadline: 9/18/2023) Update the docker image to support RISC-V (qemu-user) and Cortex-M (qemu). Add test programs for these architectures. The image supports x86/x64/Cortex-A now.
- [Doniyor] (Deadline: 9/18/2023) Install ohmyzsh theme for the zsh shell. And change zsh as the default shell.
- [Matt] (Deadline: 10/7/2023) Make the website publicly accesible. Need to talk with CSE IT to figure out how it works. May need to (1) get a public IP? (2) HTTPS certificate.
- [Amelia] (Deadline: 10/7/2023) Explore other deployment options. Considering 5,000 registered users world-wide and 1,000 active. 
- [Matt] (Deadline: 9/18/2023) We have added a "user history" button for "admin" to see each user's histroy input. However, there is a bug as the feature only works for user "elijah". Understand how this feature is implemented and fix the bug so the admin can see everyone's history.
- [Doniyor] (Deadline: 9/18/2023) Tutorials page: There should a tutorials page, where we can add documents, vedios, youtube links, slides etc.
- [] (Deadline: 10/7/2023) Do a presentation on the database table of CTFd and PwnCollege.
- [] (Deadline: 9/18/2023) Design the create-challenges database tables.
- [Amelia] (Deadline: 9/18/2023) There are still many "pwncollege" and "CTFd" in the docs/xml/pages. Go through each occurrence and check if we can replace with Pwn.IoT. 
- [] (Deadline: 9/18/2023) The forget password feature is not working. Fix it.

## GUI

- [] (Deadline: ???, 2023; Elijah) Develop a theme: Check the pwn college website and their source code, we need to develop similar theme on our own.
- [] (Deadline: ???, 2023; Elijah) About: Create a credit page to list all of the contributors to the platform (names, pictures). The page should be easily updateable, if possible include admin access to update the credit page. Admin edit access from the platform will allow to update without modifying source code.
- [] (Deadline: ???, 2022; Developer) Statistics page: Modify the statistics page that will show CTF-Challenges, Defense Challenges, Create Challenges solved by a user.
- [] (Deadline: ???, 2022; Developer) Defense Challenges: Create a defense challenges page that will show all the defense challenges. This page will be similar to the CTF-Challenges page. It will include a flag capture test script and a functional requirement test provided by us, to check if the submitted solution maintains the functional requirements and if the bug is fixed. The provided Defense Challenges will capture a flag by default, but if the user fixes these bugs of the challenges it will not get the default flag. There should also be a way (scripts to automate submission compilation) for the user to interact with the platform to submit the challenges.
- [] (Deadline: ???, 2022; Developer) Create Challenges: Create Challenges page should give the users some kind of interaction method to design the challenges. After designing the challenge the users will submit it to the platform, our interaction method will update the challenge as CTF-Challenges or Defensive Challenges. The user who creates the challenge needs to solve the challenge first and submit an exploit on the platform. Lastly, there should be admin access to the submitted challenge source code and exploit to review those.
- [] (Deadline: ???, 2022; Developer) User discussion page:** Create a discussion page or discord server like pwn college where users can discuss about the challenges.
- [] (Deadline: ???, 2022; Developer) In-page discussion feature:

## For the todo-list of Challenges. Please refer to https://github.com/CactiLab/CTF-challenges