# Github actions implementation

Hello visitor! I am [Breno D. Chrispim](https://github.com/DChrispim) and this repository is dedicated to my implementation of GitHub Actions, with the inclusion of the execution of a Python script that generates an output file every time a specific folder is modified in this repository. This tries to mimic an actual workflow or data pipeline where the modification of the file inside the input folder (with the addition of numbers) triggers the GitHub Actions to process this file, generating an output file (in the output folder) that indicates if the numbers are odd/even. The new file is automatically committed by the GitHub bot.

## Folder structure & implementation
This project includes an [python script](src/scripts/python_script.py), an [requirements file](requirements.txt) and a [Action script](.github/workflows/run-script.yml) in the following folder structure:
```bash
├── .github
│   └── workflows
│       └── run-script.yml
├── src
|   └── input
|   └── output
│   └── scripts
│       └── autp_anki_card_creation.py
├── requirements.txt
```

It is important to notice that in order for the bot to be able to make the commit, it is necessary to give the permission to do so. One way is to follow the steps
1. Access the repository settings
2. In Actions, go to the General section
3. In Workflow, permissions include the 'Read and write' check.

## About me

I chose to study physics to understand the natural world, and I am passionate about the challenges of learning it. Beyond a deep understanding of Physics, my academic experience has taught me to have a methodical approach to problems and to work in collaborative research, improving not only my communication skills, but also my ability to organize projects.

After finishing my PhD, I continued my journey by growing my knowledge of machine learning and programming with Python. My main goal is to use all my academic background in the industry, migrating from theoretical to practical research, and see the results of my work applied in real-world scenarios.

## My skills

### Programming Languages

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)

### Software Development

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

### Frameworks & Libraries

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/SeaBorn-%3670A0.svg?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

### FrontEnd

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)

### General

![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)
![Jira](https://img.shields.io/badge/jira-%230A0FFF.svg?style=for-the-badge&logo=jira&logoColor=white)

### Languages

**Native:** ![Portuguese](https://img.shields.io/badge/Portuguese-green)
**Fluent:** ![English](https://img.shields.io/badge/English-blue)
**Basic:** ![Alemão](https://img.shields.io/badge/Alemão-red)

## Contact me on

<div>
<a href = "mailto:brenoadsdc@gmail.com"><img loading="lazy" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
<a href="https://www.linkedin.com/in/brenochrispim/" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
<a href="https://dchrispim.github.io/my-portfolio/" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/My%20github%20page-121013?style=for-the-badge&logo=github&logoColor=white" target="_blank"></a>
</div>

## My stats on GitHub

<div>
<a href="https://github.com/DChrispim/"></a>
<img loading="lazy" height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=DChrispim&layout=compact&langs_count=7&theme=dracula"/>
<img loading="lazy" height="180em" src="https://github-readme-stats.vercel.app/api?username=DChrispim&show_icons=true&theme=dracula&include_all_commits=true&count_private=true"/>
</div>

## Credits

- [**Markdown Badges**](https://github.com/Ileriayo/markdown-badges)
