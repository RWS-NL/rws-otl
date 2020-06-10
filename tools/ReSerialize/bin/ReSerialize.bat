@rem
@rem Copyright 2015 the original author or authors.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem      https://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.
@rem

@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  ReSerialize startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%..

@rem Add default JVM options here. You can also use JAVA_OPTS and RE_SERIALIZE_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS=

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if "%ERRORLEVEL%" == "0" goto init

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto init

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:init
@rem Get command-line arguments, handling Windows variants

if not "%OS%" == "Windows_NT" goto win9xME_args

:win9xME_args
@rem Slurp the command line arguments.
set CMD_LINE_ARGS=
set _SKIP=2

:win9xME_args_slurp
if "x%~1" == "x" goto execute

set CMD_LINE_ARGS=%*

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\lib\airbim-otl-git-tools-0.1-SNAPSHOT.jar;%APP_HOME%\lib\commons-cli-1.4.jar;%APP_HOME%\lib\owlapi-apibinding-5.1.14.jar;%APP_HOME%\lib\slf4j-simple-1.7.30.jar;%APP_HOME%\lib\owlapi-impl-5.1.14.jar;%APP_HOME%\lib\owlapi-oboformat-5.1.14.jar;%APP_HOME%\lib\owlapi-rio-5.1.14.jar;%APP_HOME%\lib\owlapi-parsers-5.1.14.jar;%APP_HOME%\lib\owlapi-tools-5.1.14.jar;%APP_HOME%\lib\owlapi-api-5.1.14.jar;%APP_HOME%\lib\hppcrt-0.7.5.jar;%APP_HOME%\lib\caffeine-2.6.1.jar;%APP_HOME%\lib\guava-22.0.jar;%APP_HOME%\lib\jsr305-3.0.2.jar;%APP_HOME%\lib\rdf4j-rio-jsonld-2.3.2.jar;%APP_HOME%\lib\jsonld-java-0.12.0.jar;%APP_HOME%\lib\rdf4j-rio-n3-2.3.2.jar;%APP_HOME%\lib\rdf4j-rio-nquads-2.3.2.jar;%APP_HOME%\lib\rdf4j-rio-ntriples-2.3.2.jar;%APP_HOME%\lib\rdf4j-rio-rdfjson-2.3.2.jar;%APP_HOME%\lib\rdf4j-rio-rdfxml-2.3.2.jar;%APP_HOME%\lib\rdf4j-rio-trix-2.3.2.jar;%APP_HOME%\lib\rdf4j-rio-trig-2.3.2.jar;%APP_HOME%\lib\rdf4j-rio-turtle-2.3.2.jar;%APP_HOME%\lib\rdf4j-rio-languages-2.3.2.jar;%APP_HOME%\lib\rdf4j-rio-datatypes-2.3.2.jar;%APP_HOME%\lib\rdf4j-rio-binary-2.3.2.jar;%APP_HOME%\lib\rdf4j-rio-api-2.3.2.jar;%APP_HOME%\lib\rdf4j-model-2.3.2.jar;%APP_HOME%\lib\rdf4j-util-2.3.2.jar;%APP_HOME%\lib\jcl-over-slf4j-1.7.25.jar;%APP_HOME%\lib\slf4j-api-1.7.30.jar;%APP_HOME%\lib\commons-io-2.6.jar;%APP_HOME%\lib\xz-1.6.jar;%APP_HOME%\lib\commons-rdf-api-0.5.0.jar;%APP_HOME%\lib\javax.inject-1.jar;%APP_HOME%\lib\error_prone_annotations-2.0.18.jar;%APP_HOME%\lib\j2objc-annotations-1.1.jar;%APP_HOME%\lib\animal-sniffer-annotations-1.14.jar;%APP_HOME%\lib\jackson-databind-2.9.5.jar;%APP_HOME%\lib\jackson-core-2.9.5.jar;%APP_HOME%\lib\httpclient-osgi-4.5.5.jar;%APP_HOME%\lib\httpclient-cache-4.5.5.jar;%APP_HOME%\lib\httpmime-4.5.5.jar;%APP_HOME%\lib\fluent-hc-4.5.5.jar;%APP_HOME%\lib\httpclient-4.5.5.jar;%APP_HOME%\lib\httpcore-osgi-4.4.9.jar;%APP_HOME%\lib\httpcore-nio-4.4.9.jar;%APP_HOME%\lib\httpcore-4.4.9.jar;%APP_HOME%\lib\jackson-annotations-2.9.0.jar;%APP_HOME%\lib\commons-codec-1.10.jar

@rem Execute ReSerialize
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %RE_SERIALIZE_OPTS%  -classpath "%CLASSPATH%" nl.rws.otl.git_tools.ReSerialize %CMD_LINE_ARGS%

:end
@rem End local scope for the variables with windows NT shell
if "%ERRORLEVEL%"=="0" goto mainEnd

:fail
rem Set variable RE_SERIALIZE_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
if  not "" == "%RE_SERIALIZE_EXIT_CONSOLE%" exit 1
exit /b 1

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega
