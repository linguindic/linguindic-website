# Converting Linguistic Notion Word Doc to a DB HTML entry

This dir is used to help you convert a Word doc of a Linguistic Notion into the proper format to be added to the database via the admin dashboard

- General Tips:
    - Look at examples in this dir to see how HTML should be structured
    - Look at 'Description' field for existing db Linguistic Notion entries for further examples of how to structure the HTML
    - DO IT IN DEV FIRST - only paste to live when confident and ready to show John

- Steps:
    - Copy word doc content into: https://wordhtml.com/
    - Paste output into a new .html file in VS Code
    - Make suitable adjustments:
        - Remove empty <p> elements, e.g. <p>&nbsp;</p>
        - Remove unwanted &nbsp;
        - Convert quote tags, regex find & replace on: &rsquo;|&lsquo;|’|‘  --> '
        - Convert &ndash; to -
        - Add links to related data, e.g. <a href="/data/browse/linguisticnotions/4/">'Argument structure'</a>
        - Convert section headers to <h3> (may be marked up as <u> as underlined or <p> in the Word doc) and add . after numbers, e.g. "<h3>1. Header Text</h3>"
        - Footnotes
            - Ensure footnotes set up and linking properly, e.g. <a href="#_ftn1" name="_ftnref1">[1]</a>
            - Add <hr> separator between footnotes and main content
        - Diagrams and examples
            - If simple examples, just wrap in <div class="example"><label>(1)</label><div class="content">example content here</div></div>
            - If needing to align in a grid then use table within the example container, e.g. <div class="example"><label>(6)</label><div class="content">
                <table class="no-borders">
                    <tr>
                        <td>devadattaḥ</td>
                        <td>paraśunā</td>
                        <td>chinatti.</td>
                    </tr>
                    <tr>
                        <td>D.NOM</td>
                        <td>axe.INSTR.SG</td>
                        <td>cut.PRES.3SG</td>
                    </tr>
                </table></div></div>
            - If more complicated, convert to images:
                - Screenshot in Word, edit in Photoshop
                - PNG format with transparent backgrounds
                - Font colour to match colour on page (brown: #)
                - Sample html for image (note class and style): <img src="/static/images/researchdata/linguistic_notions/relative_clauses_1.png" alt="Relative clauses diagram"  class="example" style="width: 70%">
                - Ensure font-size of image roughly matches the rest of the page (not too big/small)
    - Add a new Linguistic Notion db entry in the admin dashboard:
        - Name to start with upper case, e.g. "Argument structure"
        - Paste the HTML into the description
        - Check output on public facing part of website
        - Update "Author (in citation)" to John, otherwise will default to me as the creator
        - Upload images to core/static/researchdata/linguistic_notions with appropriate name, e.g. 'relative_clauses_1.png', 'relative_clauses_2.png', ...
