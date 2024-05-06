<img src="images/prereq/phData_banner.png" width=1200px>

## SNOWFLAKE PREREQUISITES
**You'll need a Snowflake account with a user created with ACCOUNTADMIN permissions.**
This user will be used to get things set up in Snowflake.
- It is strongly recommended to sign up for a free 30 day trial Snowflake account for this lab. Once you’ve
registered, you’ll get an email that will bring you to Snowflake so that you can sign in.
- **Make sure to Activate your account** and pick a username and password that you will remember. This will
be important for logging in later on.
- **Anaconda Terms & Conditions accepted. See Getting Started section in [Third-Party Packages](https://docs.snowflake.com/en/developer-guide/udf/python/udf-python-packages#getting-started).**
- **Snowflake Marketlace Terms accepted**

## GITHUB PREREQUISITES

### Fork and Clone Repository for Quickstart
You’ll need to create a fork of the repository for this lab in your GitHub account, which if you are reading this file you've likely already done that. However, you can check for updates to the repository and lab by visiting phData’s
[Data Engineering Pipelines with Snowpark Python](https://github.com/phdata/sfguide-data-engineering-with-snowpark-python/) associated GitHub Repository and click on the Fork
button near the top right. Complete any required fields and click Create Fork.

<img src="images/prereq/fork.png" width=800px>

By default GitHub Actions disables any workflows (or CI/CD pipelines) defined in the forked repository.
This repository contains a workflow to deploy your Snowpark Python UDF and stored procedures, which
we’ll use later on. So for now enable this workflow by opening your forked repository in GitHub, clicking on
the Actions tab near the top middle of the page, and then clicking on the I understand my workflows, go
ahead and enable them green button.

### GitHub Actions

In order for your GitHub Actions workflow to be able to connect to your Snowflake account you will need to store your Snowflake credentials in GitHub. Action Secrets in GitHub are used to securely store values/variables which will be used in your CI/CD pipelines. In this step, we will create secrets for each of the parameters.

- From the repository, click on the `Settings` tab near the top of the page. From the Settings page, click on the `Secrets and variables` then `Actions` tab in the left-hand navigation. The Actions secrets should be selected. For each secret listed below click on `New repository secret` near the top right and enter the name given below along with the appropriate value (adjusting as appropriate).

    Secret Name | Secret Value
    ------------|--------------
    SNOWFLAKE_ACCOUNT | \<myaccount\>
    SNOWFLAKE_USER | \<myusername\>
    SNOWFLAKE_PWD | \<mypassword\>
    SNOWFLAKE_ROLE | HOL_ROLE
    SNOWFLAKE_WAREHOUSE | HOL_WH
    SNOWFLAKE_DATABASE | HOL_DB

- Notes:
    - To get the SNOWFLAKE_ACCOUNT, there are a few different ways to get this, but the easiest way to get the account info in the correct format is to open a snowflake worksheet and run the following query, which will output ```<organization-accountname>```
    
    ```
    select SPLIT_PART(t.value:host::varchar, '.', 1) as org_account_name
    from table(flatten(input => parse_json(SYSTEM$ALLOWLIST()))) as t
    where t.value ilike '%SNOWFLAKE_DEPLOYMENT_REGIONLESS%'; 
    ```

### Create a GitHub Codespace

Note: Snowpark development can be done on your desktop with any IDE such as VS Code however, this lab Codespaces greatly simplifies the setup required by managing all required dependencies and automatically creating a conda environment to develop in.

<img src="images/prereq/create_codespace.png" width=600px>

- If you’ve already created a Codespace, it can be launched and stopped from this window as well.

    <img src="images/prereq/launch_codespace.png" width=600px>

   - Once the Codespace has launched and the setup script has finished, select the Snowflake icon in the left pane of the Codespace to sign into snowflake extension using your snowflake account Name then enter your username and password. You account name will be the same ```<organization-accountname>``` used for the github action.

    <img src="images/prereq/snow_ext.png" width=200px>

- The Snowflake Extension allows us to run .sql files and query snowflake from VS Code. Once you are signed into the Snowflake extension, we need to create credentials file for the Snowpark to use when running and deploying our python code. A terminal should already be open, if not open a new terminal.

    <img src="images/prereq/terminal.png" width=400px>

### Create Snowflake Credentials File
During the codespace setup a default conig file was created in the `~/.snowflake` folder

For this lab, you'll need to edit the `~/.snowflake/connections.toml` file. The easiest way to edit the default `~/.snowflake/connections.toml` file is directly from VS Code in your codespace. Type `Command-P`, type (or paste) `~/.snowflake/connections.toml` and hit return. The config file should now be open. You just need to edit the file and replace the `accountname`, `username`, and `password` with your values leaving the double quotes, which are the exact same values used for the Github secrets. `accountname` will be the same ```<organization-accountname>``` used for the previous steps.

Now **save** and close the file.

Alternatively, you can open that file by entering the following command into the same terminal: 
```
code /home/vscode/.snowflake/connections.toml
```

Note: we are creating the connection information in the codespace and not in the repostitory, so no credentials are being commited to github in this lab.

### Create Anaconda Environment and Test Connection
This lab will take place inside an Anaconda virtual environment running in the Codespace. An anaconda environment called `snowflake-demo` should already have been created for you. You will know the environment is active when you see `(snowflake-demo)`, instead of `(base)` in front of the host name.

 <img src="images/prereq/conda_env.png" width=800px>

If it is not active, then execute:
```
conda activate snowflake-demo
```

Lastly, lets test that the connection is successful. To do this we'll run `test_connection.py`

```
python test_connection.py
```

If the connection test returns successful, you have completed all the prerequisites for the lab. If it returns an error message, reopen the credentials file that you created at the [Create Snowflake Credentials File](#create-snowflake-credentials-file) step and check the account is correctly formatted and the username and password are correct.

If you have successfully completed all the steps, congratulations you are ready for the Hands on Lab! If you completed these prerequisites prior to attending the Hands on Lab, you can stop the Codespace in Github where you launched it from, or it will automatically stop after 30 mintues
