from flask import Flask, render_template

app = Flask(__name__)

###################################################################################
# Hlavne #######################################################################

@app.route('/')
@app.route('/blog')
def main_page():  # put application's code here
    return render_template('categories_intro_page_contact.html')

@app.route('/contact_me')
def contact_me():
    return render_template('contact_me.html')


@app.route('/roadmap')
def roadmap():
    return render_template('specific_blogs/learning_path.html')

###################################################################################
# kategorie #######################################################################
@app.route('/productivity')
def productivity_main():
    return render_template('blog_categories/Productivity/choose_blog_productivity.html')

@app.route('/productivity/blog_1')
def productivity_1():
    return render_template('specific_blogs/Productivity/blog_productivity_1.html')

@app.route('/productivity/blog_2')
def productivity_2():
    return render_template('specific_blogs/Productivity/blog_productivity_2.html')

@app.route('/productivity/blog_3')
def productivity_3():
    return render_template('specific_blogs/Productivity/blog_productivity_3.html')

@app.route('/productivity/blog_4')
def productivity_4():
    return render_template('specific_blogs/Productivity/blog_productivity_4.html')

@app.route('/productivity/blog_5')
def productivity_5():
    return render_template('specific_blogs/Productivity/blog_productivity_5.html')


@app.route('/web_development')
def web_dev_main():
    return render_template('blog_categories/Web/choose_blog_webdev.html')

@app.route('/web_development/blog_1')
def web_development_1():
    return render_template('specific_blogs/WebDevelopment/blog_webdev_1.html')

@app.route('/web_development/blog_2')
def web_development_2():
    return render_template('specific_blogs/WebDevelopment/blog_webdev_2.html')

@app.route('/web_development/blog_3')
def web_development_3():
    return render_template('specific_blogs/WebDevelopment/blog_webdev_3.html')

@app.route('/web_development/blog_4')
def web_development_4():
    return render_template('specific_blogs/WebDevelopment/blog_webdev_4.html')

@app.route('/web_development/blog_5')
def web_development_5():
    return render_template('specific_blogs/WebDevelopment/blog_webdev_5.html')







@app.route('/hobby')
def hobby_main():
    return render_template('blog_categories/Hobbies/choose_blog_hobbies.html')

@app.route('/hobby/blog_1')
def hobby_1():
    return render_template('specific_blogs/Hobbies/blog_hobby_1.html')

@app.route('/hobby/blog_2')
def hobby_2():
    return render_template('specific_blogs/Hobbies/blog_hobby_2.html')

@app.route('/hobby/blog_3')
def hobby_3():
    return render_template('specific_blogs/Hobbies/blog_hobby_3.html')

@app.route('/hobby/blog_4')
def hobby_4():
    return render_template('specific_blogs/Hobbies/blog_hobby_4.html')

@app.route('/hobby/blog_5')
def hobby_5():
    return render_template('specific_blogs/Hobbies/blog_hobby_5.html')

@app.route('/finances')
def finances_main():
    return render_template('blog_categories/Finances/choose_blog_finances.html')

@app.route('/finances/blog_1')
def finances_1():
    return render_template('specific_blogs/Finances/blog_finances_1.html')

@app.route('/finances/blog_2')
def finances_2():
    return render_template('specific_blogs/Finances/blog_finances_2.html')

@app.route('/finances/blog_3')
def finances_3():
    return render_template('specific_blogs/Finances/blog_finances_3.html')

@app.route('/finances/blog_4')
def finances_4():
    return render_template('specific_blogs/Finances/blog_finances_4.html')

@app.route('/finances/blog_5')
def finances_5():
    return render_template('specific_blogs/Finances/blog_finances_5.html')



@app.route('/learning')
def learning_main():
    return render_template('blog_categories/Learning/choose_blog_learning.html')

@app.route('/learning/blog_1')
def learning_1():
    return render_template('specific_blogs/Learning/blog_learning_1.html')

@app.route('/learning/blog_2')
def learning_2():
    return render_template('specific_blogs/Learning/blog_learning_1.html')

@app.route('/learning/blog_3')
def learning_3():
    return render_template('specific_blogs/Learning/blog_learning_3.html')

@app.route('/learning/blog_4')
def learning_4():
    return render_template('specific_blogs/Learning/blog_learning_4.html')

@app.route('/learning/blog_5')
def learning_5():
    return render_template('specific_blogs/Learning/blog_learning_5.html')

@app.route('/learning/blog_6')
def learning_6():
    return render_template('specific_blogs/Learning/blog_learning_6.html')

@app.route('/learning/blog_7')
def learning_7():
    return render_template('specific_blogs/Learning/blog_learning_7.html')




@app.route('/fitness')
def fitness_main():
    return render_template('blog_categories/Health/choose_blog_health.html')

@app.route('/fitness/blog_1')
def fitness_1():
    return render_template('specific_blogs/HealthFitness/blog_fitness_1.html')

@app.route('/fitness/blog_2')
def fitness_2():
    return render_template('specific_blogs/HealthFitness/blog_fitness_2.html')

@app.route('/fitness/blog_3')
def fitness_3():
    return render_template('specific_blogs/HealthFitness/blog_fitness_3.html')

@app.route('/fitness/blog_4')
def fitness_4():
    return render_template('specific_blogs/HealthFitness/blog_fitness_4.html')

@app.route('/fitness/blog_5')
def fitness_5():
    return render_template('specific_blogs/HealthFitness/blog_fitness_5.html')












###################################################################################
# specificke blogy #######################################################################





if __name__ == '__main__':
    app.run()
