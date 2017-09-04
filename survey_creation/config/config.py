"""
Config file for the script to create automated surveys
"""


class creationConfig:

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
    # This value needs to be added
    sid = '421498'
    admin_email = 'olivier.philippe@soton.ac.uk'
    additional_languages =

    global_parameters_S = [['sid', sid],
                           ['owner_id', '1'],
                           ['admin', 'Administrator'],
                           ['active', 'Y'],
                           ['adminemail', admin_email],
                           ['anonymized', 'N'],
                           ['format', 'G'],
                           ['savetimings', 'Y'],
                           ['template', 'ubuntu_orange'],
                           ['language', 'en'],
                           ['datestamp', 'Y'],
                           ['usecookie', 'N'],
                           ['allowregister', 'N'],
                           ['allowsave', 'Y'],
                           ['autonumber_start', '15'],
                           ['autoredirect', 'N'],
                           ['allowprev', 'N'],
                           ['printanswers', 'Y'],
                           ['ipaddr', 'Y'],
                           ['refurl', 'Y'],
                           ['datecreated', '2017-05-24'],
                           ['publicstatistics', 'N'],
                           ['publicgraphs', 'N'],
                           ['listpublic', 'N'],
                           ['htmlemail', 'N'],
                           ['sendconfirmation', 'Y'],
                           ['tokenanswerspersistence', 'N'],
                           ['assessments', 'N'],
                           ['usecaptcha', 'N'],
                           ['usetokens', 'N'],
                           ['bounce_email', admin_email],
                           ['tokenlength', '15'],
                           ['showxquestions', 'N'],
                           ['showgroupinfo', 'B'],
                           ['shownoanswer', 'Y'],
                           ['showqnumcode', 'N'],
                           ['bounceprocessing', 'N'],
                           ['showwelcome', 'Y'],
                           ['showprogress', 'Y'],
                           ['questionindex', '0'],
                           ['navigationdelay', '0'],
                           ['nokeyboard', 'N'],
                           ['alloweditaftercompletion', 'N'],
                           ['googleanalyticsstyle', '0']]


    # List of parameters that comprise the survey title and the welcome text


SL		surveyls_title		DEMO -- RSE Survey -- 2017 -- EN		en
SL		surveyls_welcometext
<h1 style="text-align: center;">[THIS IS FOR DEMO PURPOSE ONLY  -- PLEASE DO NOT SHARE]</h1>    <p> </p>    <p><strong>The purpose of this survey is to collect information about people who develop software that is used in research. We call these people<em> <a href="https://www.software.ac.uk/blog/2016-11-17-not-so-brief-history-research-software-engineers">Research Software Engineers </a></em><a href="https://www.software.ac.uk/blog/2016-11-17-not-so-brief-history-research-software-engineers">(RSEs)</a>, but they use many different job titles (including postdoctoral researcher and research assistant).</strong></p>    <h2>Why did I receive this invitation?</h2>    <p>You have received this link because you are a member of the UK RSE Association or you were identified as someone working in an RSE role. There is currently little reliable information about the RSE community, so we have been asked to collect this information to help funders and other research organisations develop policies that will support RSEs. This questionnaire gives you the opportunity to express your views about your current job and give us information about your career path.</p>    <p>Please note that this research is not compulsory and even if you decide to participate you can withdraw at any moment.</p>    <h2>How long will it take?</h2>    <p>There is a maximum of 64 questions in this survey. It takes about 10 to 15 minutes to complete.</p>    <h2>Who is responsible for this survey?</h2>    <p>This study is conducted by the University of Southampton on behalf of the<span style="line-height: 1.6em;"> </span><a href="http://software.ac.uk/" style="line-height: 1.6em;" target="_blank">Software Sustainability Institute</a> and complies with University of Southampton ethics guidelines (reference no.: ERGO/FPSE/25269).<span style="line-height: 1.6em;"> The investigators are </span><a href="mailto:s.hettrick@software.ac.uk" style="line-height: 1.6em;" target="_blank">Simon Hettrick</a><span style="line-height: 1.6em;"> and </span><a href="mailto:olivier.philippe@soton.ac.uk" style="line-height: 1.6em;" target="_blank">Olivier Philippe</a><span style="line-height: 1.6em;">. </span><span style="line-height: 1.6em;">The survey is hosted on Limesurvey servers in Germany and respects the provisions of the </span><a href="https://www.gov.uk/data-protection/the-data-protection-act" style="line-height: 1.6em;" target="_blank">Data Protection Act</a><span style="line-height: 1.6em;">. These records are anonymised and access is strictly protected and granted to the main researchers only. The results of the survey will be released publicly but only after they have been processed to ensure that individual respondents can not be identified. The results will be released under a <a href="https://creativecommons.org/licenses/by-nc/2.5/scotland/">Creative Commons by attribution, non-commercial licence</a>.</span></p>    <p>If you would like more information about the research or about the data collection, please contact <a href="mailto:olivier.philippe@soton.ac.uk" target="_blank">Olivier Philippe</a>.</p>    <p>If you have a concern or would like to make a complaint, please contact <a href="mailto:s.hettrick@software.ac.uk" target="_blank">Simon Hettrick</a>.</p>  		en
SL		surveyls_endtext		<p>Thank you for your participation. If you are interested in the outcomes of this survey, please keep an eye on the <a href="https://www.software.ac.uk">Software Sustainability Institute's website</a>. You can also get updates by joining the <a href="http://www.rse.ac.uk/join.html" target="_blank">UK RSE Association</a>.</p>    <p> </p>  		en
SL		surveyls_email_invite_subj		Invitation to participate in a survey		en
SL		surveyls_email_invite		Dear {FIRSTNAME},  you have been invited to participate in a survey.  The survey is titled: "{SURVEYNAME}"  "{SURVEYDESCRIPTION}"  To participate, please click on the link below.  Sincerely,  {ADMINNAME} ({ADMINEMAIL})  ---------------------------------------------- Click here to do the survey: {SURVEYURL}  If you do not want to participate in this survey and don't want to receive any more invitations please click the following link: {OPTOUTURL}  If you are blacklisted but want to participate in this survey and want to receive invitations please click the following link: {OPTINURL}		en
SL		surveyls_email_remind_subj		Reminder to participate in a survey		en
SL		surveyls_email_remind		Dear {FIRSTNAME},  Recently we invited you to participate in a survey.  We note that you have not yet completed the survey, and wish to remind you that the survey is still available should you wish to take part.  The survey is titled: "{SURVEYNAME}"  "{SURVEYDESCRIPTION}"  To participate, please click on the link below.  Sincerely,  {ADMINNAME} ({ADMINEMAIL})  ---------------------------------------------- Click here to do the survey: {SURVEYURL}  If you do not want to participate in this survey and don't want to receive any more invitations please click the following link: {OPTOUTURL}		en
SL		surveyls_email_register_subj		Survey registration confirmation		en
SL		surveyls_email_register		Dear {FIRSTNAME},  You, or someone using your email address, have registered to participate in an online survey titled {SURVEYNAME}.  To complete this survey, click on the following URL:  {SURVEYURL}  If you have any questions about this survey, or if you did not register to participate and believe this email is in error, please contact {ADMINNAME} at {ADMINEMAIL}.		en
SL		surveyls_email_confirm_subj		Confirmation of your participation in our survey		en
SL		surveyls_email_confirm		Dear {FIRSTNAME},  this email is to confirm that you have completed the survey titled {SURVEYNAME} and your response has been saved. Thank you for participating.  If you have any further questions about this email, please contact {ADMINNAME} on {ADMINEMAIL}.  Sincerely,  {ADMINNAME}		en
SL		surveyls_dateformat		2		en
SL		email_admin_notification_subj		Response submission for survey {SURVEYNAME}		en
SL		email_admin_notification		Hello,  A new response was submitted for your survey '{SURVEYNAME}'.  Click the following link to reload the survey: {RELOADURL}  Click the following link to see the individual response: {VIEWRESPONSEURL}  Click the following link to edit the individual response: {EDITRESPONSEURL}  View statistics by clicking here: {STATISTICSURL}		en
SL		email_admin_responses_subj		Response submission for survey {SURVEYNAME} with results		en
SL		email_admin_responses		Hello,  A new response was submitted for your survey '{SURVEYNAME}'.  Click the following link to reload the survey: {RELOADURL}  Click the following link to see the individual response: {VIEWRESPONSEURL}  Click the following link to edit the individual response: {EDITRESPONSEURL}  View statistics by clicking here: {STATISTICSURL}   The following answers were given by the participant: {ANSWERTABLE}		en
SL		surveyls_numberformat		0		en
