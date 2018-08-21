"""
Config file for the script to create automated surveys
"""


class creationConfig:

    # default_language
    languages = ['en']
    # This headers are the ones created for the tsv file.
    main_headers = ['class', 'type/scale', 'name', 'relevance', 'text', 'help', 'language', 'validation',
                    'mandatory', 'other', 'default', 'same_default', 'allowed_filetypes', 'alphasort',
                    'answer_width', 'array_filter', 'array_filter_exclude', 'array_filter_style',
                    'assessment_value', 'category_separator', 'choice_title', 'code_filter', 'commented_checkbox',
                    'commented_checkbox_auto', 'cssclass', 'date_format', 'date_max', 'date_min',
                    'display_columns', 'display_rows', 'display_type', 'dropdown_dates',
                    'dropdown_dates_minute_step', 'dropdown_dates_month_style', 'dropdown_prefix',
                    'dropdown_prepostfix', 'dropdown_separators', 'dropdown_size', 'dualscale_headerA',
                    'dualscale_headerB', 'em_validation_q', 'em_validation_q_tip', 'em_validation_sq',
                    'em_validation_sq_tip', 'equals_num_value', 'equation', 'exclude_all_others',
                    'exclude_all_others_auto', 'hidden', 'hide_tip', 'input_boxes', 'label_input_columns',
                    'location_city', 'location_country', 'location_defaultcoordinates', 'location_mapheight',
                    'location_mapservice', 'location_mapwidth', 'location_mapzoom', 'location_nodefaultfromip',
                    'location_postal', 'location_state', 'max_answers', 'max_filesize', 'max_num_of_files',
                    'max_num_value', 'max_num_value_n', 'max_subquestions', 'maximum_chars', 'min_answers',
                    'min_num_of_files', 'min_num_value', 'min_num_value_n', 'multiflexible_checkbox',
                    'multiflexible_max', 'multiflexible_min', 'multiflexible_step', 'num_value_int_only',
                    'numbers_only', 'other_comment_mandatory', 'other_numbers_only', 'other_replace_text',
                    'page_break', 'parent_order', 'prefix', 'printable_help', 'public_statistics', 'random_group',
                    'random_order', 'rank_title', 'repeat_headings', 'reverse', 'samechoiceheight',
                    'samelistheight', 'scale_export', 'show_comment', 'show_grand_total', 'show_title',
                    'show_totals', 'showpopups', 'slider_accuracy', 'slider_custom_handle', 'slider_default',
                    'slider_handle', 'slider_layout', 'slider_max', 'slider_middlestart', 'slider_min',
                    'slider_orientation', 'slider_rating', 'slider_reset', 'slider_separator',
                    'slider_showminmax', 'statistics_graphtype', 'statistics_showgraph', 'statistics_showmap',
                    'suffix', 'text_input_columns', 'text_input_width', 'time_limit', 'time_limit_action',
                    'time_limit_countdown_message', 'time_limit_disable_next', 'time_limit_disable_prev',
                    'time_limit_message', 'time_limit_message_delay', 'time_limit_message_style',
                    'time_limit_timer_style', 'time_limit_warning', 'time_limit_warning_2',
                    'time_limit_warning_2_display_time', 'time_limit_warning_2_message',
                    'time_limit_warning_2_style', 'time_limit_warning_display_time', 'time_limit_warning_message',
                    'time_limit_warning_style', 'use_dropdown', 'value_range_allows_missing']

    # List of parameters that needs to be added at the start of the survey. They are all under the value 'S' for the key 'class'

    global_headers = [{'class': 'S', 'name': 'sid', 'text': '421498'},
                      {'class': 'S', 'name': 'owner_id', 'text': '1'},
                      {'class': 'S', 'name': 'admin', 'text': 'Administrator'},
                      {'class': 'S', 'name': 'active', 'text': 'Y'},
                      {'class': 'S', 'name': 'adminemail', 'text': 'orp2c15@soton.ac.uk'},
                      {'class': 'S', 'name': 'anonymized', 'text': 'N'},
                      {'class': 'S', 'name': 'format', 'text': 'G'},
                      {'class': 'S', 'name': 'savetimings', 'text': 'Y'},
                      {'class': 'S', 'name': 'template', 'text': 'ubuntu_orange'},
                      {'class': 'S', 'name': 'language', 'text': 'en'},
                      {'class': 'S', 'name': 'datestamp', 'text': 'Y'},
                      {'class': 'S', 'name': 'usecookie', 'text': 'N'},
                      {'class': 'S', 'name': 'allowregister', 'text': 'N'},
                      {'class': 'S', 'name': 'allowsave', 'text': 'N'},
                      {'class': 'S', 'name': 'autonumber_start', 'text': '15'},
                      {'class': 'S', 'name': 'autoredirect', 'text': 'N'},
                      {'class': 'S', 'name': 'allowprev', 'text': 'N'},
                      {'class': 'S', 'name': 'printanswers', 'text': 'Y'},
                      {'class': 'S', 'name': 'ipaddr', 'text': 'Y'},
                      {'class': 'S', 'name': 'refurl', 'text': 'Y'},
                      {'class': 'S', 'name': 'datecreated', 'text': '2018-09-03'},
                      {'class': 'S', 'name': 'publicstatistics', 'text': 'N'},
                      {'class': 'S', 'name': 'publicgraphs', 'text': 'N'},
                      {'class': 'S', 'name': 'listpublic', 'text': 'N'},
                      {'class': 'S', 'name': 'htmlemail', 'text': 'N'},
                      {'class': 'S', 'name': 'sendconfirmation', 'text': 'Y'},
                      {'class': 'S', 'name': 'tokenanswerspersistence', 'text': 'N'},
                      {'class': 'S', 'name': 'assessments', 'text': 'N'},
                      {'class': 'S', 'name': 'usecaptcha', 'text': 'N'},
                      {'class': 'S', 'name': 'usetokens', 'text': 'N'},
                      {'class': 'S', 'name': 'bounce_email', 'text': 'orp2c15@soton.ac.uk'},
                      {'class': 'S', 'name': 'tokenlength', 'text': '15'},
                      {'class': 'S', 'name': 'showxquestions', 'text': 'N'},
                      {'class': 'S', 'name': 'showgroupinfo', 'text': 'B'},
                      {'class': 'S', 'name': 'shownoanswer', 'text': 'Y'},
                      {'class': 'S', 'name': 'showqnumcode', 'text': 'N'},
                      {'class': 'S', 'name': 'bounceprocessing', 'text': 'N'},
                      {'class': 'S', 'name': 'showwelcome', 'text': 'Y'},
                      {'class': 'S', 'name': 'showprogress', 'text': 'Y'},
                      {'class': 'S', 'name': 'questionindex', 'text': '0'},
                      {'class': 'S', 'name': 'navigationdelay', 'text': '0'},
                      {'class': 'S', 'name': 'nokeyboard', 'text': 'N'},
                      {'class': 'S', 'name': 'alloweditaftercompletion', 'text': 'N'},
                      {'class': 'S', 'name': 'googleanalyticsstyle', 'text': '0'}]

    # List of parameters that comprise the survey title and the welcome text
    global_settings = [{'class': 'SL', 'name': 'surveyls_welcometext', 'text': None, 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_endtext', 'text': None, 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_email_invite_subj', 'text': 'Invitation to participate in a survey', 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_email_invite', 'text': """Dear {FIRSTNAME},  you have been invited to participate in a survey.  The survey is titled: "{SURVEYNAME}"  "{SURVEYDESCRIPTION}"  To participate, please click on the link below.  Sincerely,  {ADMINNAME} ({ADMINEMAIL})  ---------------------------------------------- Click here to do the survey: {SURVEYURL}  If you do not want to participate in this survey and don't want to receive any more invitations please click the following link: {OPTOUTURL}  If you are blacklisted but want to participate in this survey and want to receive invitations please click the following link: {OPTINURL}""", 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_email_remind_subj', 'text': """Reminder to participate in a survey""", 'language': 'en'},

                       {'class': 'SL', 'name': 'surveyls_email_remind', 'text': """Dear {FIRSTNAME},  Recently we invited you to participate in a survey.  We note that you have not yet completed the survey, and wish to remind you that the survey is still available should you wish to take part.  The survey is titled: "{SURVEYNAME}"  "{SURVEYDESCRIPTION}"  To participate, please click on the link below.  Sincerely,  {ADMINNAME} ({ADMINEMAIL})  ---------------------------------------------- Click here to do the survey: {SURVEYURL}  If you do not want to participate in this survey and don't want to receive any more invitations please click the following link: {OPTOUTURL}""", 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_email_register', 'text': """Dear {FIRSTNAME},  You, or someone using your email address, have registered to participate in an online survey titled {SURVEYNAME}.  To complete this survey, click on the following URL:  {SURVEYURL}  If you have any questions about this survey, or if you did not register to participate and believe this email is in error, please contact {ADMINNAME} at {ADMINEMAIL}.""", 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_email_confirm_subj', 'text': """Confirmation of your participation in our survey""", 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_email_confirm', 'text': """Dear {FIRSTNAME},  this email is to confirm that you have completed the survey titled {SURVEYNAME} and your response has been saved. Thank you for participating.  If you have any further questions about this email, please contact {ADMINNAME} on {ADMINEMAIL}.  Sincerely,  {ADMINNAME}""", 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_dateformat', 'text': '2', 'language': 'en'},
                       {'class': 'SL', 'name': 'email_admin_notification_subj', 'text': """Response submission for survey {SURVEYNAME}""", 'language': 'en'},
                       {'class': 'SL', 'name': 'email_admin_notification', 'text': """Hello,  A new response was submitted for your survey '{SURVEYNAME}'.  Click the following link to reload the survey: {RELOADURL}  Click the following link to see the individual response: {VIEWRESPONSEURL}  Click the following link to edit the individual response: {EDITRESPONSEURL}  View statistics by clicking here: {STATISTICSURL}""", 'language': 'en'},
                       {'class': 'SL', 'name': 'email_admin_responses_subj', 'text': """Response submission for survey {SURVEYNAME} with results""", 'language': 'en'},
                       {'class': 'SL', 'name': 'email_admin_responses', 'text': """Hello,  A new response was submitted for your survey '{SURVEYNAME}'.  Click the following link to reload the survey: {RELOADURL}  Click the following link to see the individual response: {VIEWRESPONSEURL}  Click the following link to edit the individual response: {EDITRESPONSEURL}  View statistics by clicking here: {STATISTICSURL}   The following answers were given by the participant: {ANSWERTABLE}""", 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_numberformat', 'text': '0', 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_policy_notice', 'text': "", 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_policy_error', 'text': "", 'language': 'en'},
                       {'class': 'SL', 'name': 'surveyls_policy_notice_label', 'text': "", 'language': 'en'}]

    # Standard layout for groups
    group_format = {'class': 'G', 'type/scale': 'G+inc_number', 'relevance': '1'}

    # Standard layout for questions
    one_choice_question = {'class': 'Q', 'type/scale': '!', 'relevance': '1', 'same_default': '1', 'statistics_showgraph': '1', 'time_limit_action': 1}
    one_choice_answer = {'class': 'A', 'type/scale': '0'}

    ranking_question = {'class': 'Q', 'type/scale': 'R', 'relevance': '1', 'other': 'N', 'same_default': '1', 'max_subquestions': '5', 'samechoiceheight': '1', 'samelistheight': '1', 'showpopups': '1', 'statistics_showgraph': '1'}

    ranking_answer = {'class': 'A', 'type/scale': '0'}

    multiple_choice_question = {'class': 'Q', 'type/scale': 'M', 'relevance': '1', 'same_default': '1',
                                'assessment_value': '1', 'display_columns': '1', 'statistics_showgraph': '1',
                                'default': 'Y', 'allowed_filetypes': '1',
                                'category_separator': '1', 'display_rows': '1', 'statistics_showmap': '1'}

    multiple_choice_answer = {'class': 'SQ', 'type/scale': '0'}

    freenumeric_question = {'class': 'Q', 'type/scale': 'N', 'allowed_filetypes': '1', 'statistics_showmap': '1'}

    freetext_question = {'class': 'Q', 'type/scale': 'S', 'relevance': '1'}

    likert_question = {'class': 'Q', 'type/scale': 'F', 'same_default': '1', 'statistics_showgraph': '1'}

    likert_answer = {'class': 'A', 'type/scale': '0'}

    y_n_question = {'class': 'Q', 'type/scale': 'Y', 'relevance': '1', 'same_default': '1', 'statistics_showgraph': '1'}

    datetime_question = {'class': 'Q', 'type/scale': 'D', 'same_default': '1', 'dropdown_dates_minute_step': '1',
                         'statistics_showgraph': '1'}
    subquestion = {'class': 'SQ', 'type/scale': '0'}
