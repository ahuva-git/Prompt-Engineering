# 🧠 Prompt Engineering Project – Natural Language to CMD Agent

---

## 📌 Project Overview

This project demonstrates an iterative prompt engineering process in which a language model converts natural language instructions into Windows CMD commands.

The goal is to analyze how different prompt designs affect accuracy, safety, and consistency of outputs.

---

## ⚙️ Project Structure

- `main.py` – Python script for the CLI agent using OpenAI API  
- `prompt.txt` – baseline prompt  
- `prompt2.txt` – improved prompt with clearer rules  
- `prompt3.txt` – strict constrained prompt  

---

## 🧪 Methodology

The project follows an iterative prompt engineering workflow:

1. Create an initial prompt  
2. Test with 15 natural language inputs  
3. Run the agent and collect outputs  
4. Evaluate results:
   - correctness
   - safety
   - format consistency  
5. Improve the prompt based on observed failures  
6. Repeat for 3 iterations  

---

## 📊 Evaluation Data

All test cases and results are documented in Google Sheets:

👉 https://docs.google.com/spreadsheets/d/1uG_7AqH7frtdv_v0GlyI34xsHwMrbdYBPN6gmFPmCV8/edit?usp=sharing

Each iteration includes:
- 15 test prompts  
- model output  
- expected output  
- safety evaluation  
- correctness score  

---

## 🧾 Safety Design

The system blocks or prevents dangerous commands such as:

- Disk formatting  
- Deletion (rmdir /s /q)  
- System shutdown or restart  

The model returns `BLOCKED` or `ERROR` when necessary.

---

## 🚀 How to Run

Install dependencies and run:

```bash
uv run main.py




# 🧠 פרויקט הנדסת פרומפטים – המרת שפה טבעית לפקודות CMD

---

## 📌 סקירה כללית

הפרויקט מדגים תהליך איטרטיבי של הנדסת פרומפטים, שבו מודל שפה ממיר הוראות בשפה טבעית לפקודות CMD של Windows.

המטרה היא לבדוק כיצד שינויים בפרומפט משפיעים על:
- דיוק הפלט
- בטיחות הפקודות
- עקביות התוצאות

---

## ⚙️ מבנה הפרויקט

- `main.py` – קובץ פייתון להרצת הסוכן (CLI)  
- `prompt.txt` – פרומפט בסיסי  
- `prompt2.txt` – פרומפט משופר עם כללים ברורים יותר  
- `prompt3.txt` – פרומפט קשיח ומוגבל  

---

## 🧪 מתודולוגיית עבודה

הפרויקט מבוסס על תהליך איטרטיבי של הנדסת פרומפטים:

1. יצירת פרומפט ראשוני  
2. בדיקה עם 15 תרחישים בשפה טבעית  
3. הרצת המודל וקבלת פלטים  
4. תיעוד התוצאות בגיליון Google Sheets  
5. הערכת ביצועים לפי:
   - דיוק
   - בטיחות
   - עקביות פורמט  
6. שיפור הפרומפט בהתאם לכשלים  
7. חזרה על התהליך בשלוש איטרציות  

---

## 📊 נתוני הערכה

כל תרחישי הבדיקה והתוצאות מתועדים ב־:

👉 https://docs.google.com/spreadsheets/d/1uG_7AqH7frtdv_v0GlyI34xsHwMrbdYBPN6gmFPmCV8/edit?usp=sharing

בכל איטרציה יש:
- 15 תרחישי בדיקה  
- פלט של המודל  
- פלט צפוי  
- הערכת תקינות  
- בדיקת בטיחות  

---

## 🧾 עקרונות בטיחות

המערכת חוסמת פקודות מסוכנות כגון:

- פירמוט דיסק  
- מחיקה (rmdir /s /q)  
- כיבוי או הפעלה מחדש של המחשב  

במקרים אלו מוחזר:
- `BLOCKED` או `ERROR`

---

## 🚀 איך מריצים

```bash
uv run main.py