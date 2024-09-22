{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "# Task : 1 Titanic Survival Prediction\n",
    "\n",
    "#### Data Science Internship at CodeSoft\n",
    "\n",
    "> Author : Yogesh Baghel\n",
    "\n",
    "> Batch : Sep\\-Oct\n",
    "\n",
    "> Domain : Data Science\n",
    ">\n",
    "> ---\n",
    "\n",
    "### Task : TITANIC SURVIVAL PREDICTION\n",
    "\n",
    "- Use the Titanic dataset to build a model that predicts whether a passenger on the Titanic survived or not. This is a classic beginner project with readily available data. \n",
    "- The dataset typically used for this project contains information about individual passengers, such as their age, gender, ticket class, fare, cabin, and whether or not they survived.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "## Data Description\n",
    "\n",
    "- **pclass**: A proxy for socio\\-economic status \\(SES\\)\n",
    "- - 1st = Upper\n",
    "  - 2nd = Middle\n",
    "  - 3rd = Lower\n",
    "- **age**: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5\n",
    "- **sibsp**: The dataset defines family relations in this way...\n",
    "- - Sibling = brother, sister, stepbrother, stepsister\n",
    "  - Spouse = husband, wife \\(mistresses and fiancés were ignored\\)\n",
    "- **parch**: The dataset defines family relations in this way...\n",
    "- - Parent = mother, father\n",
    "  - Child = daughter, son, stepdaughter, stepson Some children travelled only with a nanny, therefore parch=0 for them.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>892</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Kelly, Mr. James</td>\n",
       "      <td>male</td>\n",
       "      <td>34.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>330911</td>\n",
       "      <td>7.8292</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>893</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Wilkes, Mrs. James (Ellen Needs)</td>\n",
       "      <td>female</td>\n",
       "      <td>47.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>363272</td>\n",
       "      <td>7.0000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>894</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Myles, Mr. Thomas Francis</td>\n",
       "      <td>male</td>\n",
       "      <td>62.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>240276</td>\n",
       "      <td>9.6875</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>895</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Wirz, Mr. Albert</td>\n",
       "      <td>male</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>315154</td>\n",
       "      <td>8.6625</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>896</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Hirvonen, Mrs. Alexander (Helga E Lindqvist)</td>\n",
       "      <td>female</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3101298</td>\n",
       "      <td>12.2875</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>413</th>\n",
       "      <td>1305</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Spector, Mr. Woolf</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A.5. 3236</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>414</th>\n",
       "      <td>1306</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Oliva y Ocana, Dona. Fermina</td>\n",
       "      <td>female</td>\n",
       "      <td>39.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17758</td>\n",
       "      <td>108.9000</td>\n",
       "      <td>C105</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>415</th>\n",
       "      <td>1307</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Saether, Mr. Simon Sivertsen</td>\n",
       "      <td>male</td>\n",
       "      <td>38.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>SOTON/O.Q. 3101262</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>416</th>\n",
       "      <td>1308</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Ware, Mr. Frederick</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>359309</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>417</th>\n",
       "      <td>1309</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Peter, Master. Michael J</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2668</td>\n",
       "      <td>22.3583</td>\n",
       "      <td>NaN</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>418 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass  \\\n",
       "0            892         0       3   \n",
       "1            893         1       3   \n",
       "2            894         0       2   \n",
       "3            895         0       3   \n",
       "4            896         1       3   \n",
       "..           ...       ...     ...   \n",
       "413         1305         0       3   \n",
       "414         1306         1       1   \n",
       "415         1307         0       3   \n",
       "416         1308         0       3   \n",
       "417         1309         0       3   \n",
       "\n",
       "                                             Name     Sex   Age  SibSp  Parch  \\\n",
       "0                                Kelly, Mr. James    male  34.5      0      0   \n",
       "1                Wilkes, Mrs. James (Ellen Needs)  female  47.0      1      0   \n",
       "2                       Myles, Mr. Thomas Francis    male  62.0      0      0   \n",
       "3                                Wirz, Mr. Albert    male  27.0      0      0   \n",
       "4    Hirvonen, Mrs. Alexander (Helga E Lindqvist)  female  22.0      1      1   \n",
       "..                                            ...     ...   ...    ...    ...   \n",
       "413                            Spector, Mr. Woolf    male   NaN      0      0   \n",
       "414                  Oliva y Ocana, Dona. Fermina  female  39.0      0      0   \n",
       "415                  Saether, Mr. Simon Sivertsen    male  38.5      0      0   \n",
       "416                           Ware, Mr. Frederick    male   NaN      0      0   \n",
       "417                      Peter, Master. Michael J    male   NaN      1      1   \n",
       "\n",
       "                 Ticket      Fare Cabin Embarked  \n",
       "0                330911    7.8292   NaN        Q  \n",
       "1                363272    7.0000   NaN        S  \n",
       "2                240276    9.6875   NaN        Q  \n",
       "3                315154    8.6625   NaN        S  \n",
       "4               3101298   12.2875   NaN        S  \n",
       "..                  ...       ...   ...      ...  \n",
       "413           A.5. 3236    8.0500   NaN        S  \n",
       "414            PC 17758  108.9000  C105        C  \n",
       "415  SOTON/O.Q. 3101262    7.2500   NaN        S  \n",
       "416              359309    8.0500   NaN        S  \n",
       "417                2668   22.3583   NaN        C  \n",
       "\n",
       "[418 rows x 12 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data = pd.read_csv(\"tested.csv\")\n",
    "titanic_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>892</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Kelly, Mr. James</td>\n",
       "      <td>male</td>\n",
       "      <td>34.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>330911</td>\n",
       "      <td>7.8292</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>893</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Wilkes, Mrs. James (Ellen Needs)</td>\n",
       "      <td>female</td>\n",
       "      <td>47.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>363272</td>\n",
       "      <td>7.0000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>894</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Myles, Mr. Thomas Francis</td>\n",
       "      <td>male</td>\n",
       "      <td>62.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>240276</td>\n",
       "      <td>9.6875</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>895</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Wirz, Mr. Albert</td>\n",
       "      <td>male</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>315154</td>\n",
       "      <td>8.6625</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>896</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Hirvonen, Mrs. Alexander (Helga E Lindqvist)</td>\n",
       "      <td>female</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3101298</td>\n",
       "      <td>12.2875</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0          892         0       3   \n",
       "1          893         1       3   \n",
       "2          894         0       2   \n",
       "3          895         0       3   \n",
       "4          896         1       3   \n",
       "\n",
       "                                           Name     Sex   Age  SibSp  Parch  \\\n",
       "0                              Kelly, Mr. James    male  34.5      0      0   \n",
       "1              Wilkes, Mrs. James (Ellen Needs)  female  47.0      1      0   \n",
       "2                     Myles, Mr. Thomas Francis    male  62.0      0      0   \n",
       "3                              Wirz, Mr. Albert    male  27.0      0      0   \n",
       "4  Hirvonen, Mrs. Alexander (Helga E Lindqvist)  female  22.0      1      1   \n",
       "\n",
       "    Ticket     Fare Cabin Embarked  \n",
       "0   330911   7.8292   NaN        Q  \n",
       "1   363272   7.0000   NaN        S  \n",
       "2   240276   9.6875   NaN        Q  \n",
       "3   315154   8.6625   NaN        S  \n",
       "4  3101298  12.2875   NaN        S  "
      ]
     },
     "execution_count": 4,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 418 entries, 0 to 417\n",
      "Data columns (total 12 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   PassengerId  418 non-null    int64  \n",
      " 1   Survived     418 non-null    int64  \n",
      " 2   Pclass       418 non-null    int64  \n",
      " 3   Name         418 non-null    object \n",
      " 4   Sex          418 non-null    object \n",
      " 5   Age          332 non-null    float64\n",
      " 6   SibSp        418 non-null    int64  \n",
      " 7   Parch        418 non-null    int64  \n",
      " 8   Ticket       418 non-null    object \n",
      " 9   Fare         417 non-null    float64\n",
      " 10  Cabin        91 non-null     object \n",
      " 11  Embarked     418 non-null    object \n",
      "dtypes: float64(2), int64(5), object(5)\n",
      "memory usage: 39.3+ KB\n"
     ]
    }
   ],
   "source": [
    "titanic_data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>418.000000</td>\n",
       "      <td>418.000000</td>\n",
       "      <td>418.000000</td>\n",
       "      <td>332.000000</td>\n",
       "      <td>418.000000</td>\n",
       "      <td>418.000000</td>\n",
       "      <td>417.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1100.500000</td>\n",
       "      <td>0.363636</td>\n",
       "      <td>2.265550</td>\n",
       "      <td>30.272590</td>\n",
       "      <td>0.447368</td>\n",
       "      <td>0.392344</td>\n",
       "      <td>35.627188</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>120.810458</td>\n",
       "      <td>0.481622</td>\n",
       "      <td>0.841838</td>\n",
       "      <td>14.181209</td>\n",
       "      <td>0.896760</td>\n",
       "      <td>0.981429</td>\n",
       "      <td>55.907576</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>892.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.170000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>996.250000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.895800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1100.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1204.750000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>39.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1309.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>76.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>512.329200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       PassengerId    Survived      Pclass         Age       SibSp  \\\n",
       "count   418.000000  418.000000  418.000000  332.000000  418.000000   \n",
       "mean   1100.500000    0.363636    2.265550   30.272590    0.447368   \n",
       "std     120.810458    0.481622    0.841838   14.181209    0.896760   \n",
       "min     892.000000    0.000000    1.000000    0.170000    0.000000   \n",
       "25%     996.250000    0.000000    1.000000   21.000000    0.000000   \n",
       "50%    1100.500000    0.000000    3.000000   27.000000    0.000000   \n",
       "75%    1204.750000    1.000000    3.000000   39.000000    1.000000   \n",
       "max    1309.000000    1.000000    3.000000   76.000000    8.000000   \n",
       "\n",
       "            Parch        Fare  \n",
       "count  418.000000  417.000000  \n",
       "mean     0.392344   35.627188  \n",
       "std      0.981429   55.907576  \n",
       "min      0.000000    0.000000  \n",
       "25%      0.000000    7.895800  \n",
       "50%      0.000000   14.454200  \n",
       "75%      0.000000   31.500000  \n",
       "max      9.000000  512.329200  "
      ]
     },
     "execution_count": 6,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId      0\n",
       "Survived         0\n",
       "Pclass           0\n",
       "Name             0\n",
       "Sex              0\n",
       "Age             86\n",
       "SibSp            0\n",
       "Parch            0\n",
       "Ticket           0\n",
       "Fare             1\n",
       "Cabin          327\n",
       "Embarked         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "### Age and Cabin has Null values or blank....\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "#  we will fill blank with median value\n",
    "titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Embarked\n",
       "S    270\n",
       "C    102\n",
       "Q     46\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Count the Embarked\n",
    "titanic_data['Embarked'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "# replace blanks with mode value\n",
    "titanic_data['Embarked'].fillna('S', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId      0\n",
       "Survived         0\n",
       "Pclass           0\n",
       "Name             0\n",
       "Sex              0\n",
       "Age              0\n",
       "SibSp            0\n",
       "Parch            0\n",
       "Ticket           0\n",
       "Fare             1\n",
       "Cabin          327\n",
       "Embarked         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# check Null value in data\n",
    "titanic_data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "# In fare column has also null value, replace with  median\n",
    "titanic_data['Fare'].fillna(titanic_data['Fare'].median(), inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "# We will remove the \"Cabin\" column because it contains a significant number of missing values.\n",
    "titanic_data.drop(columns=\"Cabin\", inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PassengerId    0\n",
      "Survived       0\n",
      "Pclass         0\n",
      "Name           0\n",
      "Sex            0\n",
      "Age            0\n",
      "SibSp          0\n",
      "Parch          0\n",
      "Ticket         0\n",
      "Fare           0\n",
      "Embarked       0\n",
      "dtype: int64\n",
      "   PassengerId  Survived  Pclass  \\\n",
      "0          892         0       3   \n",
      "1          893         1       3   \n",
      "2          894         0       2   \n",
      "3          895         0       3   \n",
      "4          896         1       3   \n",
      "\n",
      "                                           Name     Sex   Age  SibSp  Parch  \\\n",
      "0                              Kelly, Mr. James    male  34.5      0      0   \n",
      "1              Wilkes, Mrs. James (Ellen Needs)  female  47.0      1      0   \n",
      "2                     Myles, Mr. Thomas Francis    male  62.0      0      0   \n",
      "3                              Wirz, Mr. Albert    male  27.0      0      0   \n",
      "4  Hirvonen, Mrs. Alexander (Helga E Lindqvist)  female  22.0      1      1   \n",
      "\n",
      "    Ticket     Fare Embarked  \n",
      "0   330911   7.8292        Q  \n",
      "1   363272   7.0000        S  \n",
      "2   240276   9.6875        Q  \n",
      "3   315154   8.6625        S  \n",
      "4  3101298  12.2875        S  \n"
     ]
    }
   ],
   "source": [
    "# Last check null value and Dataset\n",
    "print(titanic_data.isnull().sum())\n",
    "print(titanic_data.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "## Now Data is Cleaned...\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "# Exploratory Data Analysis\n",
    "\n",
    "#### survival variable describe as\n",
    "\n",
    "0 = No, 1 = Yes\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Survived\n",
       "0    266\n",
       "1    152\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data['Survived'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Survived', ylabel='count'>"
      ]
     },
     "execution_count": 25,
     "metadata": {
     },
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 864x504 with 1 Axes>"
      ]
     },
     "execution_count": 25,
     "metadata": {
      "image/png": {
       "height": 424,
       "width": 723
      },
      "needs_background": "light"
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.countplot(data=titanic_data,x='Survived')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "### Pclass data describe as:\n",
    "\n",
    "- 1st = Upper\n",
    "- 2nd = Middle\n",
    "- 3rd = Lower\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Pclass', ylabel='count'>"
      ]
     },
     "execution_count": 26,
     "metadata": {
     },
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 864x504 with 1 Axes>"
      ]
     },
     "execution_count": 26,
     "metadata": {
      "image/png": {
       "height": 424,
       "width": 723
      },
      "needs_background": "light"
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.countplot(data=titanic_data,x='Pclass')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Sex', ylabel='count'>"
      ]
     },
     "execution_count": 27,
     "metadata": {
     },
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 864x504 with 1 Axes>"
      ]
     },
     "execution_count": 27,
     "metadata": {
      "image/png": {
       "height": 424,
       "width": 723
      },
      "needs_background": "light"
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.countplot(data=titanic_data,x='Sex')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 864x504 with 1 Axes>"
      ]
     },
     "execution_count": 35,
     "metadata": {
      "image/png": {
       "height": 424,
       "width": 723
      },
      "needs_background": "light"
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.histplot(data=titanic_data, x='Age')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "## \\# Show count of survival wrt pclass\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABacAAANRCAYAAAD3YgA3AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAABYlAAAWJQFJUiTwAABF70lEQVR4nO3deZSlZXnv7+9NtzaCjILBnyCDMqhIEIwG0DCoiBqBKFGMAxiHIw4IDpETp1bRaIIBwYjnYCI4JCAqGIw4REAFnABHRBABFRU4zDMC/fz+qF2kKaq6m+5dz+6quq61er293/Gucq2k18fXZ1drLQAAAAAA0NMqox4AAAAAAIC5R5wGAAAAAKA7cRoAAAAAgO7EaQAAAAAAuhOnAQAAAADoTpwGAAAAAKA7cRoAAAAAgO7EaQAAAAAAuhOnAQAAAADoTpwGAAAAAKA7cRoAAAAAgO7EaQAAAAAAups/6gHmoqq6NMmaSS4b8SgAAAAAACtikyQ3ttY2vb8XitOjseaDHvSgdR/96EevO+pBAAAAAACW1wUXXJDbbrttua4Vp0fjskc/+tHrnnvuuaOeAwAAAABguW2//fY577zzLluea605DQAAAABAd+I0AAAAAADdidMAAAAAAHQnTgMAAAAA0J04DQAAAABAd+I0AAAAAADdidMAAAAAAHQ3f9QDAAAAAACsqEWLFuXaa6/NTTfdlDvuuCOttVGPNONUVRYsWJA11lgj6667blZZZXrfbRanAQAAAIAZbdGiRfntb3+bW2+9ddSjzGittdx+++25/fbbc8stt2SjjTaa1kAtTgMAAAAAM9q1116bW2+9NfPnz88GG2yQ1Vdffdrf+p2NFi1alFtuuSVXXHFFbr311lx77bVZb731pu15/hMCAAAAAGa0m266KUmywQYbZI011hCml9Mqq6ySNdZYIxtssEGS//m9TtvzpvXuAAAAAADT7I477kiSrL766iOeZHYY/z2O/16nizgNAAAAAMxo419+6I3p4aiqJJn2L5X0nxYAAAAAAPcYj9PTTZwGAAAAAKA7cRoAAAAAgO7EaQAAAACAIbvssstSVdl///1HPcpKS5wGAAAAAOasqrrXn3nz5mW99dbLbrvtln//938f9Xiz2vxRDwAAAAAAMGrvete7kiR33nlnfvGLX+SLX/xiTj/99Jxzzjn553/+5xFPNzuJ0wAAAADAnLdw4cJ7ff7GN76Rpz/96TniiCNy4IEHZpNNNhnJXLOZZT0AAAAAACZ46lOfmq222iqttfzgBz+417Hvf//7ecELXpCHP/zhWbBgQR72sIdl9913z2c/+9ml3veiiy7KIYcckic84QlZf/31s2DBgmy88cZ51atelcsvv/w+57fWctxxx2XHHXfM+uuvn1VXXTUbbbRRnvGMZ+SEE06417k/+clP8sIXvjCbbLJJFixYkPXXXz/bbbddDjrooNx5550r9guZBt6cBgAAAACYRGstydi61OOOOeaYHHDAAZk3b1723HPPbL755rnqqqtyzjnn5KMf/Wie//znL/GeX/jCF/Kxj30su+66a3bcccc88IEPzPnnn5+Pf/zjOeWUU3LOOefk4Q9/+D3nv+1tb8s//MM/ZNNNN83zn//8rLXWWvnDH/6QH/zgBznxxBPzghe8IMlYmH7Sk56Uqsqee+6ZTTfdNDfeeGMuvvjifPSjH82hhx6aBzzgAdPwW1p+4jQAAAAAwAT//d//nQsvvDBVlT/7sz9Lkvz85z/Pa17zmqy55pr59re/ncc+9rH3umayN58neslLXpKDDz44CxYsuNf+r33ta3nmM5+ZQw89NEcfffQ9+//P//k/efjDH56f/exnWW211e51zdVXX33P34877rjcfvvtOfnkk7PXXnvd67zrrrvuPteuDMRpAAAAAGDOG19z+s4778yFF16Yk08+Oa21HHzwwdl4442TJEcffXTuuuuuvOMd77hPmE6SDTfccKnPWfyt6MXtvvvueexjH5uvfvWr9zn2gAc8IPPmzbvP/vXWW+8++x70oAfdZ98666yz1LlGQZwGAAAAAOa8d7/73UnGlvBYe+2185SnPCUvf/nL8+IXv/iec7773e8mSZ75zGcu93Naa/nMZz6TY489Nj/+8Y9z3XXX5e67777n+AMf+MB7nf+iF70oRx11VB7zmMfk+c9/fnbeeefssMMOWWutte513gte8IJ8+MMfzt5775199tknT3va07LTTjvlkY985HLPOt3EaQAAAABgzhtfX3pJrr/++iRTv/28LN74xjfmiCOOyMMe9rA84xnPyMMf/vB73nY+9thj8+tf//pe5x9++OHZbLPN8olPfCIf+MAH8oEPfCDz58/Ps571rHzoQx/Kox71qCTJE5/4xHz729/O+973vnzuc5/Lpz71qSTJlltumXe961154QtfuNwzTxdxGgAAAABgGay99tpJkt/97nfZaqut7vf1V111VY488shsvfXWOfvss7PGGmvc6/h//Md/3OeaefPm5aCDDspBBx2Uq666KmeeeWaOP/74nHjiiTn//PNz/vnn37N+9Q477JAvfelLueOOO3LuuefmK1/5So466qj8zd/8TdZff/087WlPu/8/9DRaZdQDAAAAAADMBH/+53+eJDn11FOX6/pLLrkkixYtyu67736fMH355ZfnkksuWeL1D33oQ/Pc5z43n/3sZ7PbbrvlV7/6VX72s5/d57wFCxZkxx13zHve854ceeSRSZIvfvGLyzXzdBKnAQAAAACWwQEHHJD58+fnve99b37+85/f5/jll1++xOs32WSTJMmZZ555r3Wmb7755rzyla/MXXfdda/z77jjjpx11ln3uc+dd96Za6+9Nkmy2mqrJUnOPvvs3Hbbbfc598orr7zXeSsTy3oAAAAAACyDxzzmMfnoRz+aV7/61Xn84x+fvfbaK5tvvnmuueaa/OAHP8iaa66Z008/fcrrN9hgg+y77745/vjjs+2222b33XfPDTfckK9//etZddVVs+222+ZHP/rRPeffdtttefKTn5xHPepR2X777bPxxhvn9ttvz9e//vVccMEF2XPPPfPoRz86SfKP//iPOe200/KUpzwlm266aR784Afn/PPPz6mnnpp11lknr3rVq6b713O/idMAAAAAAMvola98ZbbeeuscdthhOeOMM3LyySdnvfXWyzbbbJNXvOIVS73+X//1X7PZZpvlhBNOyL/8y79k/fXXz5577pn3vOc9ed7znnevc1dfffV88IMfzOmnn56zzz47J598ctZYY4088pGPzNFHH52//du/vefc17zmNVlnnXXyve99L2eeeWbuuuuubLjhhnnNa16TN73pTdl4442H/rtYUbUs30LJcFXVudttt91255577qhHAQAAAIAZ74ILLkiSe94iZsUt6+90++23z3nnnXdea237+/sMa04DAAAAANCdOA0AAAAAQHfWnAYA7rHTUTuNegQYirNef99vNAcAAFYu3pwGAAAAAKA7cRoAAAAAgO7EaQAAAAAAuhOnAQAAAADoTpwGAAAAAKA7cRoAAAAAgO7EaQAAAAAAuhOnAQAAAADo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3jh77713Xve61+UhD3nI0J61Irw5DQAAAAAwixx++OG55ZZb8vSnPz1veMMb8qIXvSjz58/PwoULs8022+S3v/3tqEdM4s1pAAAAAIBZ5cYbb8yqq656n/1ve9vb8v73vz//8A//kI9+9KMjmOzevDkNAAAAADCLTBamk+T5z39+kuSXv/xlz3GmJE4DAAAAAMwBp5xySpJkm222GfEkYyzrAQAAAAAwCx122GG5+eabc8MNN+Scc87JmWeemW222SaHHHLIqEdLIk4DAAAAAMxKhx12WK688sp7Pu+xxx459thjs/76649wqv9hWQ8AAAAAgFnoiiuuSGstV1xxRb7whS/kkksuyeMf//icd955ox4tiTgNAAAAADCr/cmf/En+6q/+Kl/72tdyzTXX5KUvfemoR0oiTgMAAAAAzAkbb7xxHvOYx+T888/P1VdfPepxxGkAAAAAgLni97//fZJk3rx5I55EnAYAAAAAmDUuuuii3HDDDffZv2jRorztbW/LVVddlR133DHrrLPOCKa7t/mjHgAAAAAAgOH48pe/nP/9v/93nvzkJ2fTTTfNQx7ykFx55ZX55je/mUsuuSQbbLBBjjnmmFGPmUScBgAAAACYNZ72tKfl4osvzplnnpkf/vCHuf7667P66qtniy22yEte8pIceOCBWXfddUc9ZhJxGgAAAACYA856/VmjHqGLrbfeOh/5yEdGPcYyseY0AAAAAADdidMAAAAAAHQnTgMAAAAA0J04DQAAAABAd+I0AAAAAADdidMAAAAAAHQnTgMAAAAAcI/WWpfniNMAAAAAwIxWVUmSRYsWjXiS2WE8To//XqeLOA0AAAAAzGgLFixIktxyyy0jnmR2GP89jv9ep4s4DQAAAADMaGussUaS5IorrshNN92URYsWdVuaYrZorWXRokW56aabcsUVVyT5n9/rdJk/rXcHAAAAAJhm6667bm655Zbceuutufzyy0c9zqyw2mqrZd11153WZ4jTAAAAAMCMtsoqq2SjjTbKtddem5tuuil33HGHN6eXQ1VlwYIFWWONNbLuuutmlVWmd+ENcRoAAAAAmPFWWWWVrLfeellvvfVGPQrLyJrTAAAAAAB0J04DAAAAANCdOA0AAAAAQHfiNAAAAAAA3YnTAAAAAAB0J04DAAAAANCdOA0AAAAAQHfiNAAAAAAA3YnT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",
      "text/plain": [
       "<Figure size 864x504 with 1 Axes>"
      ]
     },
     "execution_count": 38,
     "metadata": {
      "image/png": {
       "height": 424,
       "width": 723
      },
      "needs_background": "light"
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.countplot(x=titanic_data['Survived'], hue=titanic_data['Pclass'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "## \\# Show count of survival wrt gender\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      male\n",
       "1    female\n",
       "2      male\n",
       "3      male\n",
       "4    female\n",
       "Name: Sex, dtype: object"
      ]
     },
     "execution_count": 10,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data['Sex'].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABacAAANRCAYAAAD3YgA3AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAABYlAAAWJQFJUiTwAABGu0lEQVR4nO3de5SeVX3//c8XIkFiAAMiovDEqghaBQkKaouAleKviiBULCogVWsrFfDQ8tSi4KHaHyrikT5aRLACrQcqnrCVcBJUTBCqRjlIVKpUIQSBQIBkP3/MHZpMJuTAZE9m5vVaa9aVe1+nfcVZynpzue9qrQUAAAAAAHraaKwnAAAAAADA5CNOAwAAAADQnTgNAAAAAEB34jQAAAAAAN2J0wAAAAAAdCdOAwAAAADQnTgNAAAAAEB34jQAAAAAAN2J0wAAAAAAdCdOAwAAAADQnTgNAAAAAEB34jQAAAAAAN1NGesJTEZVdWOSzZPMH+OpAAAAAAA8FDOT/K619vi1PVGcHhubP/zhD5+x8847zxjriQAAAAAArKt58+bl7rvvXqdzxemxMX/nnXeeMWfOnLGeBwAAAADAOps1a1bmzp07f13OteY0AAAAAADdidMAAAAAAHQnTgMAAAAA0J04DQAAAABAd+I0AAAAAADdidMAAAAAAHQnTgMAAAAA0N2UsZ4AAAAAALD+LV26NAsWLMgdd9yRxYsXp7U21lNiA1NVmTp1aqZPn54ZM2Zko43W77vN4jQAAAAATHBLly7NL3/5yyxatGisp8IGrLWWe+65J/fcc0/uuuuubL/99us1UIvTAAAAADDBLViwIIsWLcqUKVOy7bbbZtq0aev9rVjGn6VLl+auu+7KzTffnEWLFmXBggXZeuut19v9/AYCAAAAwAR3xx13JEm23XbbTJ8+XZhmRBtttFGmT5+ebbfdNsn//t6st/ut16sDAAAAAGNu8eLFSZJp06aN8UwYD5b9niz7vVlfxGkAAAAAmOCWffmhN6ZZE1WVJOv9SzP9NgIAAAAA8IBlcXp9E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAGDcWrJkST75yU/mec97XmbMmJGHPexh2WabbfL0pz89r3nNa/LlL395rKfIKkwZ6wkAAAAAAKyLJUuW5EUvelG+8Y1vZMstt8yf/Mmf5HGPe1zuvffe/OhHP8rnPve5/OQnP8kBBxww1lNlBOI0AAAAADAunX322fnGN76RXXbZJRdffHG22GKLFfYvWrQo3/3ud8dodqyOZT0AAAAAgHHp8ssvT5IceeSRK4XpJNlss82yzz77rDR+9tlnZ5999smWW26ZTTfdNDvvvHPe/e53Z/HixQ8cc9ttt2XmzJmZOnVq5syZs8L5S5cuzT777JOqyllnnTXKTzV5iNMAAAAAwLi01VZbJUmuvfbaNT7nqKOOymGHHZbrr78+Bx98cN7whjdkxowZOeGEE7L//vvn/vvvT5I88pGPzNlnn52lS5fm0EMPzR133PHANU466aRcdNFFOfLII/OqV71qdB9qEhGnAQAAAIBx6aUvfWke9rCH5bTTTsurXvWqfPGLX8zPf/7zVR5/xhln5NOf/nQOOuigXHvttfnnf/7nfOADH8i3v/3tvOMd78hFF12Uj33sYw8c/+xnPzvvec97csMNN+R1r3tdkmT27Nl597vfnZ133nmFY1l74jQAAAAAMC494xnPyGc/+9k8+tGPzmc/+9kcfPDBmTlzZrbaaqscdNBBOf/881c4/tRTT82UKVNy+umn5+EPf/gK+0444YRstdVW+Zd/+ZcVxt/61rdm//33zznnnJP3vve9ecUrXpGpU6fm3HPPzWabbbben3Ei84WIAAAAAMC49bKXvSwHHXRQZs+encsuuyxXXXVVLrvsspx33nk577zzcvjhh+eMM87I3Xffnauvvjpbb711PvShD414ralTp2bevHkrjFVVzjzzzOy66675u7/7uyTJP/3TP+VpT3va+n60CU+cBgAAAADGtYc97GHZb7/9st9++yVJlixZki984Qs56qijcuaZZ+aggw7KM5/5zLTW8tvf/jYnnXTSWl3/UY96VPbaa6+cc8452WqrrawzPUos6wEAAAAATCgbb7xxXvayl+W4445Lklx44YXZYostkgwtBdJae9Cf4c4555ycc8452XrrrXPrrbfmjW98Y9fnmajEaQAAAABgQpo+fXqSpLWWRzziEXnqU5+aH/3oR1mwYMEaX+P666/P6173ujzqUY/KVVddlb322iuf+tSncs4556yvaU8a4jQAAAAAMC6dffbZ+Y//+I8sXbp0pX0333xzPvnJTyZJ9tprryTJm970ptx777056qijsnDhwpXOue222zJ37twHPt977715+ctfnjvvvDOf+cxn8rjHPS6f+9znstVWW+Uv/uIvcsMNN6yfB5skrDkNAAAAAIxL3/3ud3Pqqadm2223zR/8wR/k8Y9/fJLkxhtvzFe/+tXcfffdeclLXpJDDjkkSXLUUUdlzpw5+fjHP54nPOEJ+eM//uPssMMOWbBgQW688cZccsklefWrX53TTjstSfI3f/M3mTNnTt70pjflhS98YZLksY99bM4444y8+MUvzqGHHprLL788m2yyydj8BYxz4jQAAAAAMC69+c1vzpOe9KT853/+Z6655ppccMEFueeee7LVVltl7733zmGHHZbDDjssVfXAOR/72Mfywhe+MKeddlr+8z//MwsXLsyMGTOyww475K1vfWte+cpXJknOP//8nHrqqdl9993zvve9b4X7vuhFL8pxxx2XU045JW9961tz6qmndn3uiaJGWuCb9auq5uy22267zZkzZ6ynAgAAAMAkMG/evCTJzjvvPMYzYbxY09+ZWbNmZe7cuXNba7PW9h7WnAYAAAAAoDtxGgAAAACA7qw5zZib9dYzx3oKwDgx5+TDx3oKAAAAwCjx5jQAAAAAAN2J0wAAAAAAdCdOAwAAAADQnTgNAAAAAEB34jQAAAAAAN2J0wAAAAAAdCdOAwAAAADQnTgNAAAAAEB34jQAAAAAAN2J0wAAAAAAdCdOAwAAAAB0MH/+/FRVjjzyyLGeygZhylhPAAAAAAAYe7PeeuZYT+FBzTn58LGeAqPMm9MAAAAAAHQnTgMAAAAA0J04DQAAAABMGsuv+3zDDTfkkEMOyVZbbZXp06dnv/32yw9/+MMkyW9/+9u87nWvy2Me85hsuummeeYzn5nZs2evcK1f/epXeec735nnPve52XbbbbPJJptku+22y2GHHZYf//jHazWvRYsW5b3vfW923XXXTJs2LY94xCPy7Gc/O2efffaoPfuGxprTAAAAAMCkM3/+/Oyxxx7Zeeedc+SRR2b+/Pn50pe+lL333jtXXHFF9t9//2y++eY59NBDs2DBgpxzzjl54QtfmGuvvTY77LBDkuSSSy7J+973vuyzzz45+OCD84hHPCLXXXddPv/5z+fLX/5yvv3tb2eXXXZZ7VwWLlyYfffdN1dddVV22223HHXUUVm6dGkuuOCCHHbYYfnRj36Ud7/73ev7r6Q7cRoAAAAAmHQuvvjivPvd787b3va2B8be9a535e1vf3v22GOPvOxlL8vHP/7xbLTR0OITL3jBC3L44YfnlFNOySmnnJIk2XffffM///M/mT59+grXvvrqq/Pc5z43xx9/fL7+9a+vdi7HHntsrrrqqvzjP/5j/uZv/uaB8XvuuScHHnhg/uEf/iGHHHJIdt1111F48g2HZT0AAAAAgEln5syZOf7441cYO+KII5Ikixcvzsknn/xAmE6Sww47LFOmTMkPfvCDB8a22WablcJ0kuyyyy7Zd999M3v27Nx3330POo9bb701n/3sZ7P77ruvEKaTZNNNN80//uM/prWWz33uc2v7iBs8b04DAAAAAJPOrrvumo033niFse222y5JsuOOO64UnTfeeOM8+tGPzk033bTC+Fe/+tWcdtpp+f73v59bbrkl999//wr7b7nlljzmMY9Z5TyuvPLKLFmyJFWVE088caX9y+L2vHnz1vjZxgtxGgAAAACYdLbYYouVxqZMmbLKfcv2L/8m9Kmnnppjjz02j3zkI/OCF7wgO+ywQzbbbLNUVc4777xcffXVWbx48YPO49Zbb00yFKmvvPLKVR535513rvaZxhtxGgAAAABgLd1///058cQTs+2222bu3LkrvR19xRVXrNF1loXw4447Lh/84AdHfZ4bMmtOAwAAAACspVtuuSULFy7Mc57znJXC9J133pm5c+eu0XWe9axnZaONNsqll166Pqa5QROnAQAAAADW0jbbbJPNNtssc+bMWWHJjfvuuy/HHHNMbrnlljW+zite8Yp8//vfz7ve9a4sWbJkpWNuuOGG3HjjjaM29w2FZT0AAAAAANbSRhttlDe+8Y153/vel6c97Wl5yUteknvvvTezZ8/OggULss8++2T27NlrdK2PfvSjue666/L2t789Z511Vv7gD/4gj370o/OrX/0q8+bNy5VXXpmzzz47j3/849fzU/XlzWkAAAAAgHXwrne9Kx/4wAfy8Ic/PP/0T/+UL37xi9l9993zve99LzvssMMaX2fzzTfPxRdfnI985CPZeuut84UvfCEf/OAHM3v27EyfPj2nnHJKXvCCF6zHJxkb1Vob6zlMOlU1Z7fddtttzpw5Yz2VDcKst5451lMAxok5Jx8+1lMAAAAYl+bNm5ck2Xnnncd4JowXa/o7M2vWrMydO3dua23W2t7Dm9MAAAAAAHQnTgMAAAAA0J04DQAAAABAd+I0AAAAAADdidMAAAAAAHQnTgMAAAAA0J04DQAAAABAd+I0AAAAAADdidMAAAAAAHQnTgMAAAAA0J04DQAAAABAd+MqTlfVVlX1mqr6UlVdX1V3V9XtVXVZVf15VW007PiZVdUe5OecB7nXEVX1vaq6c3CPi6rqRev/KQEAAAAAJr4pYz2BtfSnST6R5NdJZif5RZJHJ3lpkk8leWFV/WlrrQ077+ok541wvR+OdJOqen+SNye5Kcknk2yS5OVJzq+qv26tffShPwoAAAAAwOQ1rt6cTnJtkgOSPK619orW2v/bWjsqyU5Jfpnk4AyF6uF+0Fo7cYSfzw8/sKqek6EwfUOSp7fWjmutvSHJrCQLkry/qmaun8cDAAAAANa3D3/4w3nKU56Shz/84amqfOhDHxrrKa21I488MlWV+fPnj/VU1tm4enO6tXbhKsZvrqrTkrwnyd5JvvAQbvP6wfY9rbXblrvH/Kr6WJITkrw6yTsewj0AAAAAYIPyi3c+bayn8KB2ePt/jcp1zjnnnBxzzDF5xjOekWOPPTZTp07NnnvuOSrXZu2Mqzi9GvcNtvePsG+7qvqLJFsluTXJFa21a1ZxnX0H22+MsO/rGYrT+2YN4nRVzVnFrp1Wdy4AAAAAMPq+8pWvPLDdbrvtxng2k9uEiNNVNSXJ4YOPI0XlFwx+lj/noiRHtNZ+sdzYtCSPTXJna+3XI1znusF2x4c6ZwAAAACgv1/96ldJIkxvAMbbmtOr8r4kv5/ka621C5YbX5TkXRlaL/qRg5/nZejLFPdO8q1BkF5mi8H29lXcZ9n4lmsyqdbarJF+kvxkTc4HAAAAAEbHiSeemKrK7NmzkyRV9cDPMj/5yU9y5JFHZvvtt88mm2ySRz/60TnssMPy05/+dKXrLVvz+cYbb8xHP/rRPOUpT8mmm26amTNn5h/+4R/SWkuS/Nu//Vue9axnZdq0adlmm21y9NFH5+67717peuedd15e+cpXZscdd8y0adMybdq0zJo1Kx/+8IezdOnStXrW7373uznkkEOy7bbbZpNNNsn222+fv/iLv3ggzG8oxv2b01X1xgx9geFPkrxq+X2ttd8kefuwUy6pqv2SXJZkjySvSXJqh6kCAAAAAGNk7733TpKcccYZ+fnPf553vGPFVXu/8Y1v5KUvfWnuu+++vPjFL84Tn/jE3HTTTfniF7+Yr371q5k9e3Z22223la77lre8JRdddFFe/OIXZ7/99suXv/zlvO1tb8u9996bGTNm5Pjjj8+BBx6YP/zDP8x//Md/5GMf+1iWLFmST3ziEytc5/jjj89GG22UPfbYI4997GNz++2358ILL8wxxxyTK6+8MmedddYaPefpp5+e173udZk6dWoOOOCAbL/99rnuuuvyqU99Kueff36+853vZIcddli3v8RRNq7jdFUdnaGw/OMkz2+tLViT81pr91fVpzIUp/fK/8bpZW9GbzHiif87vnCdJgwAAAAAjIm99947e++9dy666KL8/Oc/z4knnvjAvttuuy1/9md/ls022yyXXHJJnvKUpzyw74c//GH23HPPvOY1r8ncuXNXuu6cOXNyzTXX5LGPfWySoTe0n/jEJ+bkk0/OZpttljlz5mTnnXdOkixevDjPeMYzcvrpp+ekk07KNtts88B1vvrVr+YJT3jCCtdeunRpXv3qV+fMM8/M0UcfnT322ONBn/Haa6/N61//+sycOTMXX3zxA3NKkm9961vZb7/9cswxx+RLX/rSmv/FrUfjdlmPqjo2yUeS/DDJPq21m9fyEr8dbB9Y1qO1dleS/07yiKp6zAjnPGmwvXYt7wUAAAAAbKDOPPPMLFy4MCeddNIKYTpJfv/3fz+vfe1rc9VVV+XHP/7xSueecMIJK0TgLbfcMgcccEAWLVqUv/zLv3wgTCfJ1KlTc+ihh+bee+/NvHnzVrjO8DCdJBtttFGOOeaYJMkFF1yw0v7hPvGJT+S+++7LqaeeusKckuT5z39+DjjggJx//vm54447VnutHsblm9NV9bcZWmf6B0le0Fq7ZR0us+dg+7Nh4xdmaHmQ/ZN8eti+Fy53DAAAAAAwAVxxxRVJkquvvnqFN6qXufbaoXdV582bt1K83n333Vc6ftmXLc6aNWulfcui8U033bTC+K233pqTTz45X/va1/Kzn/0sd9111wr7//u//3uNn+Piiy/OlVdeudL+3/zmN1myZEmuvfbaEefW27iL01V1QpJ3JpmTZL8HW8qjqnZL8oPW2tJh489Pctzg42eHnXZahuL026rqvNbabYNzZiZ5Q5LFWTlaAwAAAADj1K233pok+eQnP/mgx915550rjW2xxcorBE+ZMmW1++67774HxhYuXJhnPvOZufHGG/OsZz0rhx9+eGbMmJEpU6Zk4cKFOfXUU7N48eI1fo6TTz55rZ9jLIyrOF1VR2QoTC9JcmmSNy7/bZoD81trZwz+/MEkT6qqy5Ms+1cRT0+y7+DPJ7TWLl/+5Nba5VX1wSRvSnJNVX0+ySZJDk0yI8lft9bmj+ZzAQAAAABjZ1lEvvrqq/P0pz+9+/0/9alP5cYbb8w73vGOld7cvuKKK3LqqaeOfOIwy57j9ttvz+abbz7a0xx1423N6ccPthsnOTbJO0b4OXK5489KclWSZyZ5bZK/ytC60f+aZK/W2rtHuklr7c1JXp3k5iSvS3J4kh8leXFr7aOj+UAAAAAAwNjac8+hFYAvvfTSMbn/9ddfnyQ5+OCDV9p38cUXr/F1xvo51ta4itOttRNba7Wan72XO/6fW2svaq3NbK09orU2tbW2Q2vt0Nbag/4n1Fo7o7X2zNbatNba9Nba81prX1nvDwkAAAAAdPXqV786W265ZU466aR873vfW2n/0qVLc9FFF623+8+cOTNJVrrHVVddlfe+971rfJ2jjz46D3vYw3Lcccc9sE728u69994NKlyPq2U9AAAAAABG21ZbbZXPf/7zOeigg7Lnnnvm+c9/fp761KemqvLLX/4yV1xxRW699dbcc8896+X+hx9+eE4++eQce+yxmT17dp70pCfluuuuy1e+8pW89KUvzbnnnrtG19lpp51y+umn56ijjspTn/rU7L///tlxxx1z33335Re/+EUuvfTSPOpRj8pPfvKT9fIca0ucBgAAAAAmvec///m55ppr8v73vz8XXHBBLr300myyySbZbrvtsu+++4645MZo2W677XLppZfm+OOPz2WXXZYLLrggO+20Uz7+8Y/nj/7oj9Y4TifJK1/5yuyyyy75wAc+kNmzZ+eb3/xmpk2blu222y6HHHJIDj300PX2HGurWmtjPYdJp6rm7LbbbrvNmTNnrKeyQZj11jPHegrAODHn5MPHegoAAADj0rx585IkO++88xjPhPFiTX9nZs2alblz585trc1a23uMqzWnAQAAAACYGMRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAHhAa63LfcRpAAAAAJjgqipJsnTp0jGeCePBsji97PdmfRGnAQAAAGCC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",
      "text/plain": [
       "<Figure size 864x504 with 1 Axes>"
      ]
     },
     "execution_count": 11,
     "metadata": {
      "image/png": {
       "height": 424,
       "width": 723
      },
      "needs_background": "light"
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.countplot(x=titanic_data['Survived'], hue=titanic_data['Sex'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "### show survival wrt Age\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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3WOmesUrXpGqyr/927/do/3SSy/NIYcckq233jprr712Nt9887zwhS/MZZddNu11rrjiijz3uc/NxhtvnPXXXz9Lly7N6aefPu3YcRNOAwAAAABz1qabbpokufzyy2f9Xocffnje+ta35jGPeUwOP/zw7LHHHtl///2zZMmS/NM//dO0wfKpp56aG264IX/8x3+ctdaafqOKBz7wgTnooIPyy1/+Ml/84hfv1X/77bfnpJNOyuabb56nPvWpd7efccYZ2XnnnfPpT386v/d7v5cjjjgiT3nKU/Kv//qv2XXXXXPRRRfd4zo//vGPs9tuu+Xkk0/O7rvvnsMPPzxbbbVV9t9///zrv/7r/fzbGT3begAAAAAAc9azn/3s/M3f/E0+9rGP5aabbsoBBxyQXXbZJQ972MNGfq+LLrooF198cbbddtt7tB900EH5+7//+5xxxhl5xjOecY++448/Pkly8MEHr/DahxxySP7+7/8+xx9/fJ75zGfeo+/zn/98rr/++rz+9a+/O+C+/vrr84IXvCDrrbdezj333Pzu7/7u3eN/+MMfZrfddsvLXvayewTUr3rVq3Ldddflfe97Xw4//PC720899dTsv//+q/4X0YmV0wAAAADAnLXTTjvlhBNOyOabb54TTjghz3nOc7LNNttk0003zQEHHJDTTjttZPf68z//83sF08n/BM8TQfSEa6+9Nl/60pey00475TGPecwKr7377rtn++23z2mnnZZly5bdo2+6gPuTn/xkbrjhhhx99NH3CKaT5NGPfnRe/vKX5+KLL86PfvSjJMk111yTL3/5y9l2223z6le/+h7j99tvvzz5yU9eYX3jYOU0AAAAADCnPe95z8sBBxyQs88+O9/4xjdy8cUX5xvf+EZOOeWUnHLKKXnJS15y9z7P98euu+46bfvSpUvvDpavv/76bLzxxkmST3/607nrrrvutYf1TA4++OC8+c1vzoknnphXvvKVSZKf//zndwfcj33sY+8ee/755ydJvve97+Woo46617Umtjm55JJL8ru/+7u5+OKLkyRPfOITs+aaa95r/J577pmvfe1rq1RnL8JpAAAAAGDOe8ADHpB99tkn++yzT5Lkrrvuymc/+9m89KUvzSc/+ckccMAB93vrii222GLGvsnB8ite8YokgxXPD3jAA/LCF75wla7/kpe8JG9961tz/PHH3x1Of/rTn86dd955r21BrrvuuiTJxz/+8RVe8ze/+U2S5MYbb0ySbL755tOOW9F7GxfbegAAAAAA886aa66Z5z3veXnd616XJDnrrLOSJGusMYg8p3t44Q033LDCa65o5fWLX/zirLHGGndvwXHxxRfnBz/4QZ7+9Kdns802W6Wat9pqq+y999654IILcumllyaZOeBesmRJksHK6dbajB8TofbE+J///OfT3vvaa69dpRp7Ek4DAAAAAPPWBhtskCRprSXJ3Vtu/PSnP73X2O985zurfZ+tt946e++9d7797W/nsssuW+UHIU41sQXI8ccfn+9+97v5/ve/n6c97Wl58IMffI9xu+22W5Lk61//+ipdd6eddkqSfOMb38hdd911r/5zzjnnPtXZg3AaAAAAAJizPvOZz+TLX/5yli9ffq++a6+99u5tL570pCcl+Z99o4899th7rJ7+6U9/mre//e33q5aJYPkTn/hEPvOZz2SzzTbLM57xjPt0jWc/+9nZcMMNc8IJJ+S44467x3UnO/TQQ7PRRhvl6KOPzgUXXHCv/uXLl98jcN5qq63yh3/4h7nqqqvyoQ996B5jTz311Dm333Riz2kAAAAAYA779re/nfe///3ZYost8sQnPjHbbrttkuSqq67K6aefnltvvTX77bdfDjzwwCTJ7//+7+dJT3pSzj333Oy6667Ze++98/Of/zynnXZa/uiP/mjaFdWr6oADDsiGG26Y973vffntb3+b17zmNXnAAx5wn66x7rrr5rnPfW4+8YlP5CMf+Ug23XTT7Lvvvvcat+mmm+bkk0/OAQcckN122y1PecpT8qhHPSpVlZ/+9Kc5//zzc9111+W22267+5wPf/jD2X333XPEEUfkzDPPzOMe97hcccUV+dznPpdnPvOZOe2001b7vc8G4TQAAAAAMGe94Q1vyHbbbZevfOUr+f73v58vfelLue2227Lppptmzz33zAtf+MK88IUvvMd+0aeeemre9KY35dRTT80HP/jBbLfddvnbv/3b7LPPPvnnf/7n1a5lvfXWuztYTu77lh4TDjnkkHziE5/Ib3/727zgBS/I2muvPe24pzzlKfn+97+fd7/73fnSl76Ur3/961l77bXz0Ic+NHvvvXee85zn3GP8dtttl29961v5y7/8y3zlK1/JOeeck8c+9rE55ZRT8stf/nLOhdM1sRcL/VTVhTvvvPPOF1544bhLAQAAAICxuOSSS5IkO+6445grYTqr+vnZZZddctFFF13UWtvlvt7DntMAAAAAAHRnWw8AYFGa/Ct/C43fjAMAAOYDK6cBAAAAAOjOymkAYFE76Jjzxl3CyJx02NJxlwAAALDKrJwGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgu7XGXQAAAAAAwOqqqnGXsEpaa+MuYc6xchoAAAAAYJ645ppr8tKXvjQPfehDs84662SbbbbJEUcckeuvv37cpd1nVk4DAAAAAPPeQcecN+4SpnXSYUtHdq2f/OQnWbp0aX7xi19kv/32yyMf+chccMEFef/7358zzjgj3/zmN7PpppuO7H6zzcppAAAAAIB54JWvfGV+8Ytf5AMf+EBOOeWUvOtd78pZZ52V173udbnsssvy5je/edwl3ifCaQAAAACAOe4nP/lJzjzzzGyzzTZ51atedY++o48+Ouuvv34+9alP5eabbx5ThfedcBoAAAAAYI47++yzkyT77LNP1ljjnrHuBhtskD322CO33HJLvvWtb42jvNUinAYAAAAAmOMuu+yyJMn2228/bf92222XJLn88su71XR/CacBAAAAAOa4G2+8MUmyZMmSafsn2m+44YZeJd1vwmkAAAAAALoTTgMAAAAAzHETK6MnVlBPNdG+0UYb9SrpfhNOAwAAAADMcTvssEOSmfeU/vGPf5xk5j2p5yLhNAAAAADAHLfXXnslSc4888wsX778Hn033XRTvvnNb2a99dbLbrvtNo7yVotwGgAAAABgjnvEIx6RffbZJ1dffXU+/OEP36PvyCOPzM0335wXv/jFWX/99cdU4X231rgLAAAAAABg5T7ykY9k6dKlee1rX5uvfvWr2XHHHfPtb387Z599drbffvu8853vHHeJ94lwGgAAAACY9046bOm4S5h1j3jEI/Kd73wnb3vb23LGGWfkC1/4QrbccsscfvjhOfLII7PxxhuPu8T7RDgNAAAAADBPbL311jn22GPHXcZICKcBAAAAgHmrtTbuElhNHogIAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO7WGncBAAAAAACrq6rGXcIqaa2Nu4Q5x8ppAAAAAIB54OSTT85rXvOa/MEf/EE23HDDVFVe9KIXjbus1WblNAAAAAAw77Vj9x13CdOqQ08f2bXe8Y535Hvf+14e9KAHZauttsqll146smuPg5XTAAAAAADzwHvf+95cfvnl+fWvf52PfvSj4y7nfrNyGgAAAABgHthrr73GXcJIWTkNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6G6tcRcAAAAAAMDKnXLKKTnllFOSJNdee22S5Pzzz88hhxySJNlss83y7ne/e0zV3XfCaQAAAABg3qtDTx93CbPuu9/9bo4//vh7tF155ZW58sorkyQPe9jD5lU4bVsPAAAAAIB54KijjkprbcaPq6++etwl3idWTgMAAAAA81ZrbdwlsJqsnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAAcLfWWpf7CKcBAAAAgO6qKkmyfPnyMVfCVBPh9MTnaLYIpwEAAACA7tZZZ50kyc033zzmSphq4nMy8TmaLcJpAAAAAKC7DTbYIEly7bXX5qabbsry5cu7bSfBvbXWsnz58tx000259tprk/zP52i2rDWrVwcAAAAAmMYmm2ySm2++ObfcckuuueaacZfDFOutt1422WSTWb2HcBoAAAAA6G6NNdbI1ltvnWXLluWmm27K7bffbuX0mFVV1llnnWywwQbZZJNNssYas7vxhnAaAAAAABiLNdZYI5tttlk222yzcZfCGNhzGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7uZdOF1VB1bVB6vq61X166pqVXXCSs5ZWlVfqKplVXVrVX2/qo6oqjVXcM4zquqcqrqxqn5TVd+uqoNH/44AAAAAABaftcZdwGp4S5LHJflNkmuSPHJFg6tqvySfTXJbkpOSLEvyzCTvTbJHkudOc86rk3wwyXVJTkhyR5IDkxxXVY9prb1xVG8GAAAAAGAxmncrp5O8Lsn2STZM8ooVDayqDZN8PMldSfZsrf1Ja+1NSR6f5PwkB1bV86ecs02Sd2cQYj+htfaq1trrkjw2yU+SvKGqdh/pOwIAAAAAWGTmXTjdWju7tfbj1lpbheEHJnlwkhNba9+ZdI3bMliBndw74H5pknWSfKi1dvWkc65P8n+GL/9sNcsHAAAAACDzMJy+j/YeHs+Ypu/cJLckWVpV66ziOV+cMgYAAAAAgNUwH/ecvi92GB4vn9rRWruzqq5K8qgkD09yySqc87OqujnJVlW1XmvtlhXdvKounKFrhftkAwAAAAAsdAt95fSS4fHGGfon2jdajXOWzNAPAAAAAMBKLPSV02PVWttluvbhiuqdO5cDAAAAADBnLPSV0ytb5TzRfsNqnDPTymoAAAAAAFZioYfTlw2P20/tqKq1kmyb5M4kV67iOVsmWT/JNSvbbxoAAAAAgJkt9HD6rOHxqdP0PSnJeknOa63dvornPG3KGAAAAAAAVsNCD6dPTvKrJM+vqidMNFbVA5O8Y/jyo1POOTbJ7UleXVXbTDpn4yR/NXz5sdkqGAAAAABgMZh3D0Ssqv2T7D98ucXwuHtVHTf8869aa29Mktbar6vq5RmE1OdU1YlJliV5VpIdhu0nTb5+a+2qqnpTkg8k+U5VnZTkjiQHJtkqyXtaa+fPzrsDAAAAAFgc5l04neTxSQ6e0vbw4UeS/EeSN050tNZOqaonJ3lzkuckeWCSK5K8PskHWmtt6g1aax+sqquH13lJBivMf5TkLa2140f5ZgAAAAAAFqN5F0631o5KctR9POebSZ5+H885Lclp9+UcAAAAAABWzULfcxoAAAAAgDlIOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0t2jC6arat6rOrKprqurWqrqyqv6lqnafYfzSqvpCVS0bjv9+VR1RVWv2rh0AAAAAYKFZFOF0Vf1Nkn9LsnOSM5K8P8lFSfZL8s2qetGU8fslOTfJk5J8LsmHkqyd5L1JTuxXOQAAAADAwrTWuAuYbVW1RZI3Jvl5kse21n4xqW+vJGcleXuSE4ZtGyb5eJK7kuzZWvvOsP2tw7EHVtXzW2tCagAAAACA1bQYVk4/LIP3+e3JwXSStNbOTnJTkgdPaj5w+PrEiWB6OPa2JG8ZvnzFrFYMAAAAALDALYZw+sdJ7kiya1VtNrmjqp6UZIMkX5nUvPfweMY01zo3yS1JllbVOrNQKwAAAADAorDgt/VorS2rqr9I8ndJflRVpyS5LskjkjwryZeTHDbplB2Gx8unudadVXVVkkcleXiSS1Z076q6cIauR96X9wAAAAAAsNAs+HA6SVpr76uqq5P8Y5KXT+q6IslxU7b7WDI83jjD5SbaNxpljQAAAAAAi8li2NYjVfXnSU5OclwGK6bXT7JLkiuTfLqq/nY27tta22W6jySXzsb9AAAAAADmiwUfTlfVnkn+JsnnW2uvb61d2Vq7pbV2UZIDkvxXkjdU1cOHp0ysjF5yr4vds/2G2akYAAAAAGDhW/DhdJJnDI9nT+1ord2S5IIM/h52GjZfNjxuP3V8Va2VZNskd2aw6hoAAAAAgNWwGMLpdYbHB8/QP9F+x/B41vD41GnGPinJeknOa63dPpryAAAAAAAWn8UQTn99ePzTqvpfkzuq6mlJ9khyW5Lzhs0nJ/lVkudX1RMmjX1gkncMX350VisGAAAAAFjg1hp3AR2cnOQrSf53kkuq6nNJrk2yYwZbflSSv2ytXZckrbVfV9XLh+edU1UnJlmW5FlJdhi2n9T9XQAAAAAALCALPpxurS2vqqcneVWS52fwEMT1Mgicv5DkA621M6ecc0pVPTnJm5M8J8kDk1yR5PXD8a3jWwAAAAAAWHAWfDidJK213yZ53/BjVc/5ZpKnz1JJAAAAAACL2mLYcxoAAAAAgDlGOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0N1Iw+mq+p2q2nAlYzaoqt8Z5X0BAAAAAJhfRr1y+qokh69kzGuH4wAAAAAAWKRGHU7X8AMAAAAAAGY0jj2nt0hy8xjuCwAAAADAHLHW/b1AVb1kStPjp2lLkjWT/E6SFyX5wf29LwAAAAAA89f9DqeTHJekDf/ckuw3/JhqYruPW5IcPYL7AgAAAAAwT40inD50eKwk/5jklCSnTjPuriTXJTm/tXbDCO4LAAAAAMA8db/D6dba8RN/rqqDk5zSWvvk/b0uAAAAAAAL1yhWTt+ttbbXKK8HAAAAAMDCtMa4CwAAAAAAYPEZeThdVU+uqn+rql9U1W+r6q5pPu4c9X0BAAAAAJg/RrqtR1Xtm8EDEddM8p9JLksiiAYAAAAA4B5GGk4nOSrJb5Ps21o7c8TXBgAAAABggRj1th6PTnKSYBoAAAAAgBUZdTj9myTLRnxNAAAAAAAWmFGH019NsvuIrwkAAAAAwAIz6nD6L5I8oqreUlU14msDAAAAALBAjPqBiEcm+fckRyd5aVV9N8kN04xrrbU/GfG9AQAAAACYJ0YdTh8y6c/bDD+m05IIpwEAAAAAFqlRh9Pbjvh6AAAAAAAsQCMNp1tr/zHK6wEAAAAAsDCN+oGIAAAAAACwUiNdOV1Vv7OqY1tr/znKewMAAAAAMH+Mes/pqzN42OHKtFm4NwAAAAAA88SoA+JPZvpweqMkj0/ysCTnJLE3NQAAAADAIjbqByIeMlNfVa2R5K1J/izJwaO8LwAAAAAA80u3ByK21pa31o7OYOuPd/W672RV9ZSq+lxVXVtVt1fVf1fVl6rq6dOMXVpVX6iqZVV1a1V9v6qOqKo1x1E7AAAAAMBC0i2cnuS8JPv0vmlV/W2SryR5QpLPJ3lPktOTPDjJnlPG7pfk3CRPSvK5JB9KsnaS9yY5sVvRAAAAAAAL1DgeSrhJkvV73rCqXp7kTUmOT/KnrbU7pvQ/YNKfN0zy8SR3JdmztfadYftbk5yV5MCqen5rTUgNAAAAALCauq6crqr/neSgJD/seM91krwzyX9mmmA6SVprv5308sAMVlOfOBFMD8fcluQtw5evmL2KAQAAAAAWvpGunK6qs1Zwn62T/M7w9dtHed+V+MMMwub3JVleVfsmeXSS25Jc0Fo7f8r4vYfHM6a51rlJbkmytKrWaa3dPjslAwAAAAAsbKPe1mPPGdpbkuuTfCnJu1trM4XYs+H3hsfbklycQTB9t6o6N8mBrbVfDpt2GB4vn3qh1tqdVXVVkkcleXiSS1Z046q6cIauR65a6QAAAAAAC9NIw+nW2jgesLgyDxke35TkR0n+IMl3k2yb5N0ZPJzxX/I/wfqS4fHGGa430b7RaMsEAAAAAFg8xvFAxN4mAvM7kzyrtXb18PUPquqAJJcleXJV7T7NFh/3S2ttl+nahyuqdx7lvQAAAAAA5pNZXelcVRtU1dZVteFs3mclbhgeL54UTCdJWmu3ZLDVSJLsOjxOrIxekulNtN8wQz8AAAAAACsx8nC6qtaqqr+sqisyCHCvTnJ9VV0xbO+9Wvuy4fGGGfqvHx7XnTJ++6kDh7Vvm8Eq7CtHVB8AAAAAwKIz0nC6qtZOcmaSdybZJslPk1wwPG4zbP/KcFwvX83ggYy/W1XTvd+JByReNTxOPKzxqdOMfVKS9ZKc11q7faRVAgAAAAAsIqNeOf36DB4seHqSHVtr27TWdm+tbZNkhySnZfBAwteP+L4zaq39x/C+v5Pk8Ml9VbVPkj/KYFX1GcPmk5P8Ksnzq+oJk8Y+MMk7hi8/OrtVAwAAAAAsbKPeYuOFSX6YZP/W2vLJHa21n1TVs5N8N8kfJ3nXiO+9Iq9KslOSv6uqfZNcnMH2HPsnuSvJy1prNw7r/HVVvTyDkPqcqjoxybIkz8ogYD85yUkdawcAAAAAWHBGvXL6/0nyxanB9IRh+xeTPGLE912h1to1SXZJ8qEk22WwgnrPDFZU79Fa++yU8ackeXKSc5M8J8lrkvw2gxXfz2+ttV61AwAAAAAsRKNeOX1HkgetZMz6GQS9XbXWfplByPyaVRz/zSRPn9WiAAAAAAAWqVGvnP5+kgOr6sHTdVbVZkkOTPK9Ed8XAAAAAIB5ZNTh9IeSPDjJBVX1J1X18Kpat6q2rapDk3x72P+hEd8XAAAAAIB5ZKTberTW/rmqHp/kL5P8/TRDKsnfttb+eZT3BQAAAABgfhn1ntNprf1VVX0+yZ8k2SnJkiQ3Jrk4yT+21s4f9T0BAAAAAJhfRh5OJ0lr7VtJvjUb1wYAAAAAYP6733tOV9XaVXVBVX21qh6wknFfrapvrWgcAAAAAAAL3ygeiPiiJLskeU9r7bczDWqt3ZHk/ybZNckfj+C+AAAAAADMU6MIp5+d5MrW2hdWNrC1dkaSHyd57gjuCwAAAADAPDWKcHqnJOfch/HnJnn8CO4LAAAAAMA8NYpwerMkP78P43+eZNMR3BcAAAAAgHlqFOH0rUkedB/GPyjJbSO4LwAAAAAA89QowumfJnnCfRj/hCT/OYL7AgAAAAAwT40inD4nye5VtdKAuqp2SbI0ydkjuC8AAAAAAPPUKMLpDyVpSf6lqnacaVBVPTLJvyS5K8lHRnBfAAAAAADmqbXu7wVaa5dV1duTHJXk4qo6OclZSa4ZDvlfSZ6S5DlJ1knyttbaZff3vgAAAAAAzF/3O5xOktba26vqziRHJnlhkhdMGVJJfpvkza21vx7FPQEAAAAAmL9GEk4nSWvt/1TVp5O8NMkeSbYcdv0syTeSHNta+49R3Q8AAAAAgPlrZOF0kgzD5yNHeU0AAAAAABaeUTwQEQAAAAAA7hPhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO7WGncBALDQVNW4S5g1rbVxlwAAAMACYeU0AAAAAADdWTkNALPkoGPOG3cJI3PSYUvHXQIAAAALjJXTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7tYadwEAwPxRVeMuAQAAgAXCymkAAAAAALpblCunq+pFST41fPny1to/TDPmGUnemGSnJGsm+fckH2mtHd+tUACYYw465rxxlzAyJx22dNwlAAAALGqLbuV0VW2d5ENJfrOCMa9OclqSRyc5IcnHkzw0yXFV9e4edQIAAAAALGSLKpyuwUaZxya5LsnHZhizTZJ3J1mW5AmttVe11l6X5LFJfpLkDVW1e5+KAQAAAAAWpkUVTid5bZK9kxya5OYZxrw0yTpJPtRau3qisbV2fZL/M3z5Z7NYIwAAAADAgrdowumq2jHJu5K8v7V27gqG7j08njFN3xenjAEAAAAAYDUsigciVtVaGTwA8T+T/NVKhu8wPF4+taO19rOqujnJVlW1XmvtlpXc98IZuh65khoAAAAAABa0RRFOJ3lbkp2SPLG1dutKxi4ZHm+cof/GJOsPx60wnAYAAAAAYHoLPpyuqt/PYLX0e1pr5/e8d2ttlxlqujDJzj1rAQAAAACYSxb0ntPD7Tw+mcEWHW9dxdMmVkwvmaF/ZSurAQAAAABYiQUdTid5UJLtk+yY5LaqahMfSY4cjvn4sO19w9eXDY/bT71YVW2ZwZYe16xsv2kAAAAAAGa20Lf1uD3JJ2bo2zmDfai/kUEgPbHlx1lJ9kjy1EltE542aQwAAAAAAKtpQYfTw4cfvmy6vqo6KoNw+vjW2j9M6jo2yZ8neXVVHdtau3o4fuMM9q5Oko/NVs0AAAAAAIvBgg6nV0dr7aqqelOSDyT5TlWdlOSOJAcm2SpjeLAiAAAAAMBCI5yeRmvtg1V1dZI3JnlJBntz/yjJW1prx4+zNgAAAACAhWDRhtOttaOSHLWC/tOSnNarHgAAAACAxWSNcRcAAAAAAMDiI5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQ3VrjLgAAYJxOOmzpuEsAAABYlKycBgAAAACgOyunAYBFrR2777hLGJk69PRxlwAAALDKrJwGAAAAAKA74TQAAAAAAN0JpwEAAAAA6M6e0wAAC0xVjbuEkWutjbsEAABgxKycBgAAAACgOyunAQAWmIOOOW/cJYzMSYctHXcJAADALLFyGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALpba9wFALC4VdW4SwAAAADGwMppAAAAAAC6s3IagDnhoGPOG3cJI3PSYUvHXQIAAADMeVZOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoLu1xl0AACxUJx22dNwlAAAAwJxl5TQAAAAAAN1ZOQ0As6Qdu++4SxiZOvT0cZcAAADAAmPlNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0N2CD6eratOqellVfa6qrqiqW6vqxqr6RlX9SVVN+3dQVUur6gtVtWx4zver6oiqWrP3ewAAAAAAWGjWGncBHTw3yUeT/CzJ2Un+M8nmSZ6d5B+SPK2qnttaaxMnVNV+ST6b5LYkJyVZluSZSd6bZI/hNQEAAAAAWE2LIZy+PMmzkpzeWls+0VhVf5XkgiTPySCo/uywfcMkH09yV5I9W2vfGba/NclZSQ6sque31k7s+i4AAAAAABaQBb+tR2vtrNbaaZOD6WH7tUk+Nny556SuA5M8OMmJE8H0cPxtSd4yfPmK2asYAAAAAGDhW/Dh9Er8dni8c1Lb3sPjGdOMPzfJLUmWVtU6s1kYAAAAAMBCthi29ZhWVa2V5CXDl5OD6B2Gx8unntNau7OqrkryqCQPT3LJSu5x4Qxdj7xv1QIAwNxVVeMuYdZMejQNAAAjtphXTr8ryaOTfKG19qVJ7UuGxxtnOG+ifaNZqgsAAAAAYMFblCunq+q1Sd6Q5NIkL56t+7TWdpnh/hcm2Xm27gsAAONw0DHnjbuEkTnpsKXjLgEAYMFbdCunq+rVSd6f5EdJ9mqtLZsyZGJl9JJMb6L9htFXBwAAAACwOCyqcLqqjkjywSQ/zCCYvnaaYZcNj9tPc/5aSbbN4AGKV85SmQAAAAAAC96iCaer6i+SvDfJdzMIpn8xw9CzhsenTtP3pCTrJTmvtXb7yIsEAAAAAFgkFkU4XVVvzeABiBcmeUpr7VcrGH5ykl8leX5VPWHSNR6Y5B3Dlx+drVoBAAAAABaDBf9AxKo6OMnbk9yV5OtJXltVU4dd3Vo7Lklaa7+uqpdnEFKfU1UnJlmW5FlJdhi2n9SnegAAAACAhWnBh9MZ7BGdJGsmOWKGMV9LctzEi9baKVX15CRvTvKcJA9MckWS1yf5QGutzVaxAAAAAACLwYIPp1trRyU5ajXO+2aSp4+6HgAAAAAAFsme0wAAAAAAzC3CaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3QmnAQAAAADoTjgNAAAAAEB3wmkAAAAAALoTTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN2tNe4CAABgZapq3CWMXGtt3CUAAMBYWTkNAAAAAEB3Vk4DADDnHXTMeeMuYWROOmzpuEsAAIA5wcppAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAultr3AUAAMBiVFXjLgEAAMbKymkAAAAAALqzchoAAMbgoGPOG3cJI3PSYUvHXQIAAPOQldMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3dlzGoA5wX6lAMxFVTXuElgFrbVxlwAArAYrpwEAAAAA6M7KaQDmhHbsvuMuYWTq0NPHXQIAI3LQMeeNu4SRmfgtpYX4ngCA+cnKaQAAAAAAuhNOAwAAAADQnXAaAAAAAIDuhNMAAAAAAHTngYgAAAuMB4QBAADzgZXTAAAAAAB0Z+U0AMAC047dd9wljEwdevq4SwAAAGaJldMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3dlzmi6qatwlzJrW2rhLAAAAFgg/OwGwmFg5DQAAAABAd1ZO09VBx5w37hJG5qTDlo67BAAAYIHysxMAi4GV0wAAAAAAdCecBgAAAACgO+E0AAAAAADd2XMaAFhl9owEAABgVKycBgAAAACgOyunAYBV1o7dd9wljEwdevq4SwAAAFjUrJwGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdrTXuAgAAYGVOOmzpuEsAAABGzMppAAAAAAC6s3IaAIA5rx2777hLGJk69PRxlwAAAHOCldMAAAAAAHQnnAYAAAAAoDvhNAAAAAAA3dlzmq5OOmzpuEtgBapq3CXMmtbauEsAAOYh378C01moPzv5uQnozcppAAAAAAC6s3Kartqx+467hJGpQ08fdwmz5qBjzht3CSNjtRMAcH/4/hVYkYXys5Ofm4BxsXIaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDt7TgOLwkJ9mjYA85f9PRmXhTj3fK8HAPOTldMAAAAAAHRn5TSwKCyUp2gn/7PaaaG8p4W4egtgVbRj9x13CSNTh54+7hK4Dxbi3Fso3xclvjcCYHGxchoAAAAAgO6E0wAAAAAAdCecBgAAAACgO3tOAwAAwByzEPeerqpxl8BKLMTPUWtt3CUAK2DlNAAAAAAA3Vk5DQAAAHNMO3bfcZcwMnXo6UmSg445b8yVjM5CXNme+BwB/Vk5DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO48EBHup6oadwkAAAAAMO9YOQ0AAAAAQHdWTsP9dNAx5427hJE56bCl4y4BAAAAgEXCymkAAAAAALoTTgMAAAAA0J1wGgAAAACA7uw5DdyLvafnB58nAAAYr4X2PflCez/A3GflNAAAAAAA3Vk5DdxLO3bfcZcwMnXo6eMuYdYslM/TQv4cAQCwsC2078kXyvtJ/JwB84WV0wAAAAAAdCecBgAAAACgO+E0AAAAAADd2XMaWBQ8dRoAYOHyvd784PMEwFRWTgMAAAAA0J2V08Ci4KnTAAALl+/15gefJwCmsnIaAAAAAIDuhNMAAAAAAHQnnAYAAAAAoDt7TgMAACNx0mFLx10CANxDVY27hJFrrY27hJFZiJ+fCQvp8zSbrJwGAAAAAKA7K6dnUFVbJXl7kqcm2TTJz5KckuTo1tr1YywNAADmpHbsvuMuYWTq0NPHXQIAI3DQMeeNu4SRWci/oeR7iMVLOD2NqnpEkvOSPCTJqUkuTbJrksOTPLWq9mitXTfGEgEAAAAA5jXbekzvIxkE069tre3fWvvL1treSd6bZIck7xxrdQAAAAAA85xweorhqul9klyd5MNTuo9McnOSF1fV+p1LAwAAAABYMITT97bX8Hhma2355I7W2k1JvplkvSS79S4MAAAAAGChqNbauGuYU6rq/yZ5Y5I3ttbeM03/h5K8KskrW2sfXcm1Lpyh63HrrrvumjvuuOP9rne+uOiii8ZdAgAAAAB0sfPOO4+7hG4uueSS3Hrrrctaa5ve13M9EPHelgyPN87QP9G+0f24x1233nrrjRdddNHV9+Ma88Ejh8dLx1oFi5k5yDiZf4ybOcg4mX+MmznIOJl/jJs5OAcssoWa2yT59eqcKJyeRa21XcZdwzhNrBxf7H8PjI85yDiZf4ybOcg4mX+MmznIOJl/jJs5yHxiz+l7m1gZvWSG/on2G2a/FAAAAACAhUk4fW+XDY/bz9C/3fB4eYdaAAAAAAAWJOH0vZ09PO5TVff4+6mqDZLskeSWJN/qXRgAAAAAwEIhnJ6itfaTJGdmsJH3q6Z0H51k/SSfaq3d3Lk0AAAAAIAFwwMRp/fKJOcl+UBVPSXJJUl+P8leGWzn8eYx1gYAAAAAMO9Va23cNcxJVbV1krcneWqSTZP8LMnnkhzdWrt+nLUBAAAAAMx3wmkAAAAAALqz5zQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E04xcVW1VVf9YVf9dVbdX1dVV9b6q2njctbEwVNWBVfXBqvp6Vf26qlpVnbCSc5ZW1ReqallV3VpV36+qI6pqzV51szBU1aZV9bKq+lxVXTGcTzdW1Teq6k+qatp/W81BRqWq/qaqvlpVPx3OpWVVdXFVHVlVm85wjvnHrKmqFw3/LW5V9bIZxjyjqs4Zfr38TVV9u6oO7l0r89/wZ4s2w8e1M5zjayAjV1VPGX4/eO3w597/rqovVdXTpxlrDjISVXXICr4GTnzcNc155iBzVrXWxl0DC0hVPSLJeUkekuTUJJcm2TXJXkkuS7JHa+268VXIQlBV303yuCS/SXJNkkcm+XRr7UUzjN8vyWeT3JbkpCTLkjwzyQ5JTm6tPbdD2SwQVfVnST6a5GdJzk7yn0k2T/LsJEsymGvPbZP+gTUHGaWquiPJRUl+lOQXSdZPsluSJyT57yS7tdZ+Omm8+cesqaqtk/wgyZpJHpTk5a21f5gy5tVJPpjkugzm4B1JDkyyVZL3tNbe2LVo5rWqujrJRkneN033b1pr754y3tdARq6q/jbJmzL4WeSLSX6V5MFJdknyldban08aaw4yMlX1+CT7z9D9B0n2TnJ6a+0Zk84xB5nThNOMVFV9Kck+SV7bWvvgpPa/S/K6JMe01v5sXPWxMFTVXhl8I3hFkidnEBBOG05X1YbDcUsy+M+R7wzbH5jkrCS7J3lBa+3ETuUzz1XV3hmEgae31pZPat8iyQVJtk5yYGvts8N2c5CRqqoHttZum6b9nUn+KslHW2uvHLaZf8yaqqokX06ybZJ/TfLGTAmnq2qbDBYr3Jxkl9ba1cP2jZP8f0kekWRpa+38rsUzbw3D6bTWtlmFsb4GMnJV9fIkf5/k+CR/2lq7Y0r/A1prvx3+2Rykm6o6P4MFC/u11j4/bDMHmfNs68HIDFdN75Pk6iQfntJ9ZAY/lLy4qtbvXBoLTGvt7Nbaj9uq/e/agRmsYjhx4h/i4TVuS/KW4ctXzEKZLFCttbNaa6dNDqaH7dcm+djw5Z6TusxBRmq6YHron4fH7Sa1mX/MptdmsELr0Ay+z5vOS5Osk+RDE8F0krTWrk/yf4YvLVxgtvgayEhV1TpJ3pnBb87dK5hOkolgesgcpIuqekwGwfR/JTl9Upc5yJwnnGaU9hoez5wmtLkpyTeTrJfBF0zoZe/h8Yxp+s5NckuSpcNvNOH+mvhh5M5JbeYgvTxzePz+pDbzj1lRVTsmeVeS97fWzl3B0BXNwS9OGQOrap3hXud/VVWHV9VeM+yb6msgo/aHGQR9/5pkeVXtW1V/MZyHu08z3hyklz8dHj/RWpu857Q5yJy31rgLYEHZYXi8fIb+H2ewsnr7JF/tUhGsYF621u6sqquSPCrJw5Nc0rMwFpaqWivJS4YvJ3/zZw4yK6rqjRns8bskg/2mn5hBMP2uScPMP0Zu+PXuUxmsHPyrlQxf0Rz8WVXdnGSrqlqvtXbLaCtlAdsigzk42VVVdWhr7WuT2nwNZNR+b3i8LcnFSR49ubOqzs1ge7dfDpvMQWZdVa2b5EVJ7kryD1O6zUHmPCunGaUlw+ONM/RPtG80+6XA3cxLenlXBj+gfKG19qVJ7eYgs+WNGWybdUQGwfQZSfaZ9ANxYv4xO96WZKckh7TWbl3J2FWdg0tm6Iepjk3ylAwC6vWTPCbJMUm2SfLFqnrcpLG+BjJqDxke35SkZfAAug2SPDbJmUmelORfJo03B+nheRnMoTMmPxR7yBxkzhNOA8D9VFWvTfKGDB769eIxl8Mi0VrborVWGQQ0z85gxcvFVbXzeCtjIauq389gtfR7PMSQcWitHT18/sPPW2u3tNZ+OHzg+t8lWTfJUeOtkAVuIkO5M8mzWmvfaK39prX2gyQHZPDQ9ifPsMUHzJaJLT2OGWsVsJqE04zSyla+TLTfMPulwN3MS2ZVVb06yfuT/CjJXq21ZVOGmIPMqmFA87kMts7aNMknJ3Wbf4zMcDuPT2bwq8FvXcXTVnUOzrSiC1bVxEOJnzSpzddARu2G4fHiyQ95TZLh1kQTvz236/BoDjKrqupRSZZm8B8jX5hmiDnInCecZpQuGx63n6F/u+Fxpj2pYTbMOC+HP2Rvm8HKhyt7FsXCUFVHJPlgkh9mEExfO80wc5AuWmv/kcF/kjyqqjYbNpt/jNKDMphLOya5raraxEcGW8wkyceHbe8bvl7RHNwyg20ZrrHfNCMwsaXR+pPafA1k1Cbm1A0z9F8/PK47Zbw5yGyZ6UGIE8xB5jzhNKN09vC4T1XdY25V1QZJ9sjgSbDf6l0Yi9pZw+NTp+l7UpL1kpzXWru9X0ksBFX1F0nem+S7GQTTv5hhqDlITw8dHid+ODH/GKXbk3xiho+Lh2O+MXw9seXHiubg06aMgftjt+FxcsDiayCj9tUM9pr+3ak/8w5NPCDxquHRHGTWVNUDM9hS8K4M/u2djjnInCecZmRaaz/J4CEQ2yR51ZTuozNYxfCp1trNnUtjcTs5ya+SPL+qnjDROPyH/B3Dlx8dR2HMX1X11gwegHhhkqe01n61guHmICNTVdtX1b1+LbOq1qiqd2bwoKbzWmsTK7fMP0amtXZra+1l030k+fxw2PHDtpOGr4/NINR+dVVtM3Gtqto4g72rk//ZjgFWqKp2rKr1p2nfJsmHhi9PmNTlayAjNfwtpdOS/E6Swyf3VdU+Sf4og1XVZwybzUFm03OTbJzki9M8CHGCOcicV621cdfAAlJVj0hyXgY/HJ+a5JIkv59krwy281jaWrtufBWyEFTV/kn2H77cIoNvAq9M8vVh269aa2+cMv7kJLclOTHJsiTPSrLDsP15zRdDVlFVHZzkuAxWKHww0++TenVr7bhJ5+wfc5ARGG4l89cZrE69Ksl1STZP8uQMHoh4bQb/YfKjSefsH/OPWVZVR2WwtcfLW2v/MKXvNUk+kMF8PSnJHUkOTLJVBg9WfGNgFQzn2RuSnJvkP5LclOQRSfZN8sAM9ls9oLV2x6Rz9o+vgYxQVW2Vwc+8W2ewkvriDLZG2D+DVdXPb619dtL4/WMOMguq6utJnpjBwzlPW8G4/WMOMocJpxm5qto6ydsz+LWRTZP8LMnnkhw9aSUXrLZJPwDP5D9aa9tMOWePJG9OsnsGP7xckeQfk3xghr25YFqrMP+S5GuttT2nnGcOcr9V1aOT/FkGP4hslWSjJDdn8B/Ap2cwn6Y+lNP8Y9atKJwe9j8zyRuT7JzBb2/+KMmHWmvH96yT+a2qnpzB18CdMligsH4Gq1S/m+RTGfyW5r1+wPU1kFGrqgcneVsGAd+WSX6dwUKZv26tXTDNeHOQkaqqHTP4t/SaJNusbB6Zg8xlwmkAAAAAALqz5zQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgO+E0AAAAAADdCacBAAAAAOhOOA0AAAAAQHfCaQAAAAAAuhNOAwDAHFdVb66qNvzYYdz1AADAKAinAQBgDquqSvKyJG3Y9PIxlgMAACMjnAYAgLltnyTbJDk+ybVJDq6qtcdaEQAAjIBwGgAA5raJldIfT/LpJJslOWC6gVW1ZVUdW1W/qKpbq+q7VXVwVe053BLkqGnO2aSq/rqqLhmec2NVfbWq9pm1dwQAAEnWGncBAADA9Kpq8yTPSnJ5a+28qvp1kjck+dMkJ00Z+5Ak5yd5WJJzk5yXZIskH0ly5gzXf1iSczJYmf31JGckWT/JM5KcUVWHtdY+PvI3BgAAEU4DAMBcdmiSByQ5Lklaaz+sqguT7FVV/09r7YpJY/86g2D6b1trfzHRWFXvS3LBDNc/fnjOC1prJ046Z6MMQusPVNXnW2s/H9UbAgCACbb1AACAOWjSgxCXJ/nkpK7jklQmPRhxuAf1C5LcmOQdk6/TWvvelPMnznlckicn+ezkYHp4zg1JjkzywCTPud9vBgAApmHlNAAAzE17J3lEki+11v5rUvs/JXlPkkOq6i2ttd8m2SHJukm+01q7aZprfSODoHuy3YfHJdPtRZ3kwcPjjqtZPwAArJBwGgAA5qY/HR6Pm9zYWltWVadlsKJ5vyQnJ1ky7J5p+43p2jcdHv9w+DGTB61KsQAAcF/Z1gMAAOaYqnpwkv2HLz9TVW3yR/5nq42JAPvXw+PmM1xyuvYbh8fDW2u1go9D7+/7AQCA6Vg5DQAAc8/BSdZOcmGS784w5llJ/ndVbZvk0iS3JnlsVW0wzdYeT5zm/G8Nj3+Q5AP3u2IAALiPrJwGAIC5Z+Jhh69srb1suo8kx2TwYMSXtdbuSHJSBtt7vGXyhYYPPnzJ1Bu01r6T5OtJnl1VL52uiKp6TFU9ZHRvCwAA/ke11sZdAwAAMFRVeyY5O8kPWmuPXcG4bZJcmeTaJL+TwR7SFwz//LUk5yXZMsnzkpyZwTYhR7bW3j7pGlslOSvJdkm+l+TbSW5IslWSxyZ5dJLdW2sTq6wBAGBkrJwGAIC5ZWLV9D+saFBr7eokX8kggH5ma+3nSZYm+WSSRyV5XZKdkrwyyaeHp/16yjWuSbJLkjcnuSvJHyd57fA6/5nksCQ/uL9vCAAApmPlNAAALHBV9c4kf5Xkqa21L427HgAASITTAACwYFTVQ1tr/z2l7TEZbPFxR5L/1Vq7bSzFAQDAFGuNuwAAAGBkvlNVVyT5YZKbM9hLet8MtvM7TDANAMBcYuU0AAAsEFV1ZAYPPtwmyQYZPNzwW0ne3Vo7Z1x1AQDAdITTAAAAAAB0t8a4CwAAAAAAYPERTgMAAAAA0J1wGgAAAACA7oTTAAAAAAB0J5wGAAAAAKA74TQAAAAAAN0JpwEAAAAA6E44DQAAAABAd8JpAAAAAAC6E04DAAAAANCdcBoAAAAAgO6E0wAAAAAAdCecBgAAAACgu/8fsueTjNxPHkwAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 864x504 with 1 Axes>"
      ]
     },
     "execution_count": 44,
     "metadata": {
      "image/png": {
       "height": 424,
       "width": 723
      },
      "needs_background": "light"
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.histplot(x=titanic_data['Age'], hue=titanic_data['Survived'], multiple='stack')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "### show survived wrt Embarked..\n",
    "\n",
    "Port of Embarkation\t\n",
    "\n",
    "- C = Cherbourg,\n",
    "- Q = Queenstown, \n",
    "- S = Southampton\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABacAAANRCAYAAAD3YgA3AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAABYlAAAWJQFJUiTwAABFR0lEQVR4nO3deZRldXnv4e8LDSiIjAoYUNCA4oAKDtAamSJBRQHFoEYFjMZZQDN4RQSM5prEGwdwiMYAigoGFEQUjQIighABxYFBhY6Q2A5MAs3Y/bt/1Clsiqoeq3+nT/XzrFVr99nje+i17PbDZu9qrQUAAAAAAHpabdgDAAAAAACw6hGnAQAAAADoTpwGAAAAAKA7cRoAAAAAgO7EaQAAAAAAuhOnAQAAAADoTpwGAAAAAKA7cRoAAAAAgO7EaQAAAAAAuhOnAQAAAADoTpwGAAAAAKA7cRoAAAAAgO5mDXuAVVFVXZPkwUnmDHkUAAAAAIDlsWWS37fWtlraA8Xp4XjwAx/4wA233XbbDYc9CAAAAADAsrr88stz++23L9Ox4vRwzNl22203vPjii4c9BwAAAADAMtthhx1yySWXzFmWYz1zGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhu1rAHAAAAAABWTQsWLMgNN9yQW265JXfeeWdaa8MeaZVWVVlrrbWy7rrrZsMNN8xqq63Ye5vFaQAAAACguwULFuTaa6/NvHnzhj0KA6213HHHHbnjjjty2223ZYsttlihgVqcBgAAAAC6u+GGGzJv3rzMmjUrm266adZZZ50Vfqcui7ZgwYLcdtttmTt3bubNm5cbbrghG2+88Qq7nt9tAAAAAKC7W265JUmy6aabZt111xWmVwKrrbZa1l133Wy66aZJ/vB7tMKut0LPDgAAAAAwiTvvvDNJss466wx5EiYa/z0Z/z1aUcRpAAAAAKC78ZcfumN65VNVSbLCX1Dpdx4AAAAAgHuNx+kVTZwGAAAAAKA7cRoAAAAAgO7EaQAAAACAaXTcccelqnLccccNe5R7rYwzidMAAAAAwEpt/vz5+eQnP5mdd945G264YdZYY4089KEPzXbbbZdXv/rV+fKXvzzsEVkGs4Y9AAAAAADAVObPn5+99torZ555ZtZff/0873nPy+abb5677rorP/nJT/K5z30uV1xxRV7wghcMe9R77bvvvtlxxx2z2WabDXuUlZo4DQAAAACstD7/+c/nzDPPzBOf+MR8+9vfznrrrXef7fPmzcuFF144pOkmt956691vTu7PYz0AAAAAgJXW+eefnyQ58MADJw2+a6+9dnbdddd7Px955JGpqpxzzjn323fOnDmpqhx44IH3WX/ggQemqnL11Vfn6KOPznbbbZcHPvCB2WWXXXLiiSemqnLooYdOOt+dd96ZDTbYIJtttlnuueeeJPd/vvMdd9yR9ddfPw996EPv3Wei17/+9amqfOUrX7nP+iuuuCIHHnhgtthii6y55prZZJNN8rKXvSxXXnnlpOf5+c9/nhe/+MXZYIMNss4662T27Nk544wzJt132MRpAAAAAGCltdFGGyVJrrrqqhV+rYMPPjiHH354nvCEJ+Tggw/OM57xjOyzzz5Zb7318rnPfW7SsHzaaaflpptuyl/8xV9k1qzJH1TxgAc8IPvvv39++9vf5mtf+9r9tt9555056aSTsskmm2TPPfe8d/2ZZ56Z7bffPp/97Gfz1Kc+NYccckh23333fPGLX8zTnva0XHLJJfc5z89+9rPsuOOOOfnkk7PTTjvl4IMPzuabb5599tknX/ziF5fzn87081gPAAAAAGCl9cIXvjD/+I//mI9//OO55ZZbsu+++2aHHXbIIx7xiGm/1iWXXJJLL700W2211X3W77///vnEJz6RM888M3vttdd9th1//PFJkgMOOGCR5z7wwAPziU98Iscff3ye//zn32fbl7/85dx4441561vfem/gvvHGG/PSl740a6+9ds4999w89rGPvXf/H//4x9lxxx3z6le/+j6B+o1vfGOuv/76fPCDH8zBBx987/rTTjst++yzz5L/g+jEndMAAAAAwErryU9+ck444YRssskmOeGEE/KiF70oW265ZTbaaKPsu+++Of3006ftWn/7t397vzCd/CE8j4focXPnzs3Xv/71PPnJT84TnvCERZ57p512yjbbbJPTTz89N9xww322TRa4P/3pT+emm27KUUcddZ8wnSSPf/zj85rXvCaXXnppfvrTnyZJrrvuuvznf/5nttpqq7zpTW+6z/577713dt5550XONwzunAYAAAAAVmp//ud/nn333Tdnn312zjvvvFx66aU577zzcuqpp+bUU0/NK1/5ynuf87w8nva0p026fvbs2feG5RtvvDEbbLBBkuSzn/1s5s+ff79nWE/lgAMOyGGHHZYTTzwxb3jDG5Ikv/71r+8N3Nttt929+15wwQVJkh/+8Ic58sgj73eu8cecXH755XnsYx+bSy+9NEnyzGc+M6uvvvr99t9ll13y7W9/e4nm7EWcBgAAAABWemussUb22GOP7LHHHkmS+fPn55RTTsmrXvWqfPrTn86+++673I+u2HTTTafctnBYfv3rX59k7I7nNdZYIy972cuW6PyvfOUrc/jhh+f444+/N05/9rOfzT333HO/x4Jcf/31SZJPfvKTizznrbfemiS5+eabkySbbLLJpPst6rsNi8d6AAAAAAAjZ/XVV8+f//mf59BDD02SnHXWWUmS1VYbS56TvbzwpptuWuQ5F3Xn9Ste8Yqsttpq9z6C49JLL82PfvSjPPe5z83GG2+8RDNvvvnm2W233XLRRRfliiuuSDJ14F5vvfWSjN053Vqb8mc8ao/v/+tf/3rSa8+dO3eJZuxJnAYAAAAARta6666bJGmtJcm9j9y49tpr77fv97///WW+zhZbbJHddtstF154Ya688solfhHiROOPADn++OPzgx/8IJdddlme85zn5CEPech99ttxxx2TJN/5zneW6LxPfvKTkyTnnXde5s+ff7/t55xzzlLN2YM4DQAAAACstD7/+c/nP//zP7NgwYL7bZs7d+69j7141rOeleQPz40+9thj73P39LXXXpt3v/vdyzXLeFj+1Kc+lc9//vPZeOONs9deey3VOV74whfmwQ9+cE444YQcd9xx9znvwg466KCsv/76Oeqoo3LRRRfdb/uCBQvuE5w333zzPPvZz84111yTY4455j77nnbaaSvd86YTz5wGAAAAAFZiF154YT70oQ9l0003zTOf+cxstdVWSZJrrrkmZ5xxRm6//fbsvffe2W+//ZIkT3/60/OsZz0r5557bp72tKdlt912y69//eucfvrp+bM/+7NJ76heUvvuu28e/OAH54Mf/GDuvvvuvPnNb84aa6yxVOd44AMfmBe/+MX51Kc+lY9+9KPZaKON8rznPe9++2200UY5+eSTs++++2bHHXfM7rvvnsc97nGpqlx77bW54IILcv311+eOO+6495iPfOQj2WmnnXLIIYfkG9/4Rp74xCfm5z//eb70pS/l+c9/fk4//fRl/u4rgjgNAAAAAKy03va2t2XrrbfON7/5zVx22WX5+te/njvuuCMbbbRRdtlll7zsZS/Ly172svs8L/q0007L3/zN3+S0007L0Ucfna233jr/9E//lD322CNf+MIXlnmWtdde+96wnCz9Iz3GHXjggfnUpz6Vu+++Oy996Uuz5pprTrrf7rvvnssuuyzvf//78/Wvfz3f+c53suaaa+ZhD3tYdtttt7zoRS+6z/5bb711vve97+Xtb397vvnNb+acc87Jdtttl1NPPTW//e1vV7o4XePPYqGfqrp4++233/7iiy8e9igAAAAAMBSXX355kmTbbbcd8iRMZkl/f3bYYYdccskll7TWdljaa3jmNAAAAAAA3XmsBwAwchb+z/UAYDr4r4oBoD93TgMAAAAA0J07pwGAkbX/v54/7BEAGHEnvXb2sEcAgFWWO6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhu1rAHAAAAAABYVlU17BGWSGtt2COsdNw5DQAAAAAwIq677rq86lWvysMe9rCstdZa2XLLLXPIIYfkxhtvHPZoS82d0wAAAADAyNv/X88f9giTOum1s6ftXL/4xS8ye/bs/OY3v8nee++dxzzmMbnooovyoQ99KGeeeWa++93vZqONNpq2661o7pwGAAAAABgBb3jDG/Kb3/wmH/7wh3Pqqafmfe97X84666wceuihufLKK3PYYYcNe8SlIk4DAAAAAKzkfvGLX+Qb3/hGttxyy7zxjW+8z7ajjjoq66yzTj7zmc/ktttuG9KES0+cBgAAAABYyZ199tlJkj322COrrXbfrLvuuuvmGc94RubNm5fvfe97wxhvmYjTAAAAAAAruSuvvDJJss0220y6feutt06SXHXVVd1mWl7iNAAAAADASu7mm29Okqy33nqTbh9ff9NNN/UaabmJ0wAAAAAAdCdOAwAAAACs5MbvjB6/g3qi8fXrr79+r5GWmzgNAAAAALCSe/SjH51k6mdK/+xnP0sy9TOpV0biNAAAAADASm7XXXdNknzjG9/IggUL7rPtlltuyXe/+92svfba2XHHHYcx3jIRpwEAAAAAVnKPetSjsscee2TOnDn5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AAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cBAAAAAOhOnAYAAAAAoDtxGgAAAACA7sRpAAAAAAC6E6cB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",
      "text/plain": [
       "<Figure size 864x504 with 1 Axes>"
      ]
     },
     "execution_count": 45,
     "metadata": {
      "image/png": {
       "height": 424,
       "width": 723
      },
      "needs_background": "light"
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.histplot(x=titanic_data['Embarked'], hue=titanic_data['Survived'], multiple='stack')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "### Show survival wrt to Fare\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABacAAANRCAYAAAD3YgA3AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAABYlAAAWJQFJUiTwAABYTUlEQVR4nOzdeZheZX0//vcHImELBIIsFiqggLiggLUslQC2VMUFFItaF7TaalUUtf32cqnot/bbxVYF21qtClYrVKggLqAWCCouPwGJrayGqLGyhmAgJEBy//6YZ+gwzCSZyTNnttfruuY6ee5z3+d8nkzOzOSdk8+p1loAAAAAAKBLm012AQAAAAAAzD7CaQAAAAAAOiecBgAAAACgc8JpAAAAAAA6J5wGAAAAAKBzwmkAAAAAADonnAYAAAAAoHPCaQAAAAAAOiecBgAAAACgc8JpAAAAAAA6J5wGAAAAAKBzwmkAAAAAADo3Z7ILmI2q6qYk2yVZOsmlAAAAAABsij2T/Kq1ttdYFwqnJ8d2W2211Y7777//jpNdCAAAAADAeF1zzTW59957x7VWOD05lu6///47XnHFFZNdBwAAAADAuB188MG58sorl45nrZ7TAAAAAAB0TjgNAAAAAEDnhNMAAAAAAHROOA0AAAAAQOeE0wAAAAAAdE44DQAAAABA54TTAAAAAAB0bs5kFwAAAAAAzE7r1q3L8uXLs3LlyqxZsyattckuaVarqsydOzfz5s3LjjvumM02m9h7m4XTAAAAAEDn1q1bl5///OdZtWrVZJdCT2stq1evzurVq3PPPfdkjz32mNCAWjgNAAAAAHRu+fLlWbVqVebMmZNdd90122yzzYTfqcv6rVu3Lvfcc09uvvnmrFq1KsuXL89OO+00Yefz2QYAAAAAOrdy5cokya677pp58+YJpqeAzTbbLPPmzcuuu+6a5H8/RxN2vgk9OgAAAADACNasWZMk2WabbSa5EoYb/JwMfo4minAaAAAAAOjc4MMP3TE99VRVkkz4Ayp95gEAAAAAeNBgOD3RhNMAAAAAAHROOA0AAAAAQOeE0wAAAAAAfXTGGWekqnLGGWdMdikPmoo1CacBAAAAgClt7dq1+fjHP56FCxdmxx13zCMe8YjsvPPOOeCAA/Ka17wmX/ziFye7RMZhzmQXAAAAAAAwmrVr1+Y5z3lOLrzwwsyfPz/HHntsdt9999x333357//+7/zbv/1brr322jzvec+b7FIfdPzxx+eQQw7JbrvtNtmlTGnCaQAAAABgyvrc5z6XCy+8ME9+8pOzaNGibL/99g/Zv2rVqnzve9+bpOpGtv322z+sTh5OWw8AAAAAYMq6/PLLkyQnnXTSiIHv1ltvnaOOOurB16eeemqqKpdeeunD5i5dujRVlZNOOukh4yeddFKqKkuWLMnpp5+eAw44IFtttVWOPPLInHXWWamqnHLKKSPWt2bNmuywww7Zbbfd8sADDyR5eH/n1atXZ/78+dl5550fnDPc61//+lRVvvSlLz1k/Nprr81JJ52UPfbYI1tssUV22WWXvPSlL81111034nFuvPHGvOhFL8oOO+yQbbbZJocddli+/OUvjzh3sgmnAQAAAIApa8GCBUmS66+/fsLP9eY3vznvfve786QnPSlvfvObc/jhh+e4447L9ttvn3/7t38bMVg+//zzs2LFivz+7/9+5swZuVHFlltumRNPPDG33XZbvvrVrz5s/5o1a3L22Wdnl112yTOf+cwHxy+88MIcdNBB+exnP5vf+I3fyFve8pY84xnPyH/8x3/kaU97Wq688sqHHOeGG27IIYccknPOOSeHHnpo3vzmN2f33XfPcccdl//4j//YxN+d/tPWAwAAAACYsl7wghfkr//6r/PRj340K1euzPHHH5+DDz44j370o/t+riuvvDJXXXVV9tprr4eMn3jiifnYxz6WCy+8MM95znMesu/MM89Mkrzyla9c77FPOumkfOxjH8uZZ56Z5z73uQ/Z98UvfjF33nln3vrWtz4YcN955515yUtekq233jqXXXZZHv/4xz84/7/+679yyCGH5DWvec1DAuo3vOENueOOO/KhD30ob37zmx8cP//883Pcccdt/G9ER9w5DQAAAABMWQceeGA+85nPZJdddslnPvOZvPCFL8yee+6ZBQsW5Pjjj88FF1zQt3P96Z/+6cOC6eR/g+fBIHrQzTffnIsuuigHHnhgnvSkJ6332Iceemj23XffXHDBBVm+fPlD9o0UcH/605/OihUr8t73vvchwXSSPPGJT8xrX/vaXHXVVfnxj3+cJFm2bFm+/vWvZ6+99sob3/jGh8x//vOfn4ULF663vsngzmkAAAAAYEr7vd/7vRx//PG55JJL8q1vfStXXXVVvvWtb+W8887Leeedl1e84hUP9nneFE972tNGHD/ssMMeDJbvvPPO7LDDDkmSz372s1m7du3DeliP5pWvfGXe+c535qyzzsof//EfJ0luueWWBwPuAw444MG53/nOd5IkV199dU499dSHHWuwzck111yTxz/+8bnqqquSJL/1W7+VzTff/GHzjzzyyCxatGij6uyKcBoAAAAAmPIe8YhH5JhjjskxxxyTJFm7dm3OPffcvPrVr86nP/3pHH/88ZvcumLXXXcddd/QYPn1r399koE7nh/xiEfkpS996UYd/xWveEXe/e5358wzz3wwnP7sZz+bBx544GFtQe64444kycc//vH1HvPuu+9Oktx1111Jkl122WXEeet7b5NFWw8AAAAAYNrZfPPN83u/93s55ZRTkiQXX3xxkmSzzQYiz5EeXrhixYr1HnN9d16//OUvz2abbfZgC46rrroqP/rRj/LsZz87O+2000bVvPvuu+foo4/O97///Vx77bVJRg+4t99++yQDd0631kb9GAy1B+ffcsstI5775ptv3qgauyScBgAAAACmrXnz5iVJWmtJ8mDLjZ///OcPm/uDH/xg3OfZY489cvTRR+d73/terrvuuo1+EOJwgy1AzjzzzPzwhz/M4sWL86xnPSuPfOQjHzLvkEMOSZJ885vf3KjjHnjggUmSb33rW1m7du3D9l966aVjqrMLwmkAAAAAYMr63Oc+l69//etZt27dw/bdfPPND7a9OOKII5L8b9/oT33qUw+5e/rnP/953ve+921SLYPB8ic+8Yl87nOfy0477ZTnPOc5YzrGC17wgmy33Xb5zGc+kzPOOOMhxx3qVa96VebPn5/3vve9+f73v/+w/evWrXtI4Lz77rvnd37nd3LTTTflIx/5yEPmnn/++VOu33Si5zQAAAAAMIV973vfy4c//OHsuuuu+a3f+q3stddeSZKbbropX/7yl3Pvvffm+c9/fk444YQkyW/+5m/miCOOyGWXXZanPe1pOfroo3PLLbfkggsuyO/+7u+OeEf1xjr++OOz3Xbb5UMf+lDuv//+vOlNb8ojHvGIMR1jq622yote9KJ84hOfyD/+4z9mwYIFOfbYYx82b8GCBTnnnHNy/PHH55BDDskznvGMPOEJT0hV5ec//3m+853v5I477sjq1asfXPMP//APOfTQQ/OWt7wlX/va1/LkJz85N954Y77whS/kuc99bi644IJxv/eJIJwGAAAAAKast73tbdlnn33yjW98I4sXL85FF12U1atXZ8GCBTnyyCPz0pe+NC996Usf0i/6/PPPz5/8yZ/k/PPPz+mnn5599tknf/M3f5Njjjkm//7v/z7uWrbeeusHg+Vk7C09Bp100kn5xCc+kfvvvz8veclLssUWW4w47xnPeEYWL16cD3zgA7nooovyzW9+M1tssUUe9ahH5eijj84LX/jCh8zfZ5998t3vfjd/9md/lm984xu59NJLc8ABB+S8887LbbfdNuXC6RrsxUJ3quqKgw466KArrrhisksBAAAAgElxzTXXJEn233//Sa6EkWzs5+fggw/OlVdeeWVr7eCxnkPPaQAAAAAAOqetB1PeihUrsnjx4nGvP+CAAzJ//vz+FQQAAAAAbDLhNFPe4sWLs3DhwnGvX7Ro0YNPawUAAAAApgbhNNPGgSeekvm7P3aj569YdmOuOvuDE1gRAAAAADBewmmmjfm7PzY773vgZJcBAAAAAPSBByICAAAAANA54TQAAAAAAJ0TTgMAAAAA0DnhNAAAAAAAnRNOAwAAAADQOeE0AAAAAACdE04DAAAAANA54TQAAAAAAJ2bM9kFAAAAAACMV1VNdgkbpbU22SVMOe6cBgAAAACYJpYtW5ZXv/rVedSjHpW5c+dmzz33zFve8pbceeedk13amLlzGgAAAACY9k7858snu4QRnf1Hh/XtWD/5yU9y2GGH5dZbb83zn//8PO5xj8v3v//9fPjDH86FF16Yb3/721mwYEHfzjfR3DkNAAAAADAN/PEf/3FuvfXWnHbaaTnvvPPyV3/1V7n44otzyimn5Lrrrss73/nOyS5xTITTAAAAAABT3E9+8pN87Wtfy5577pk3vOEND9n33ve+N9tss03+9V//Nffcc88kVTh2wmkAAAAAgCnukksuSZIcc8wx2Wyzh8a68+bNy+GHH55Vq1blu9/97mSUNy7CaQAAAACAKe66665Lkuy7774j7t9nn32SJNdff31nNW0q4TQAAAAAwBR31113JUm23377EfcPjq9YsaKrkjaZcBoAAAAAgM4JpwEAAAAAprjBO6MH76AebnB8/vz5XZW0yYTTAAAAAABT3H777Zdk9J7SN9xwQ5LRe1JPRcJpAAAAAIAp7qij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",
      "text/plain": [
       "<Figure size 864x504 with 1 Axes>"
      ]
     },
     "execution_count": 57,
     "metadata": {
      "image/png": {
       "height": 424,
       "width": 723
      },
      "needs_background": "light"
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.histplot(x=titanic_data['Fare'], hue=titanic_data['Survived'], multiple='stack')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "## Featuring Engineering\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "#### before modeling the data, transform gender\\(Sex\\) into numeric\n",
    "\n",
    "- Male \\- 1\n",
    "- Female \\- 0\n",
    "\n",
    "**Use LabelEncoder from sklearn library**\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>892</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Kelly, Mr. James</td>\n",
       "      <td>1</td>\n",
       "      <td>34.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>330911</td>\n",
       "      <td>7.8292</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>893</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Wilkes, Mrs. James (Ellen Needs)</td>\n",
       "      <td>0</td>\n",
       "      <td>47.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>363272</td>\n",
       "      <td>7.0000</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>894</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Myles, Mr. Thomas Francis</td>\n",
       "      <td>1</td>\n",
       "      <td>62.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>240276</td>\n",
       "      <td>9.6875</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>895</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Wirz, Mr. Albert</td>\n",
       "      <td>1</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>315154</td>\n",
       "      <td>8.6625</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>896</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Hirvonen, Mrs. Alexander (Helga E Lindqvist)</td>\n",
       "      <td>0</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3101298</td>\n",
       "      <td>12.2875</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0          892         0       3   \n",
       "1          893         1       3   \n",
       "2          894         0       2   \n",
       "3          895         0       3   \n",
       "4          896         1       3   \n",
       "\n",
       "                                           Name  Sex   Age  SibSp  Parch  \\\n",
       "0                              Kelly, Mr. James    1  34.5      0      0   \n",
       "1              Wilkes, Mrs. James (Ellen Needs)    0  47.0      1      0   \n",
       "2                     Myles, Mr. Thomas Francis    1  62.0      0      0   \n",
       "3                              Wirz, Mr. Albert    1  27.0      0      0   \n",
       "4  Hirvonen, Mrs. Alexander (Helga E Lindqvist)    0  22.0      1      1   \n",
       "\n",
       "    Ticket     Fare Embarked  \n",
       "0   330911   7.8292        Q  \n",
       "1   363272   7.0000        S  \n",
       "2   240276   9.6875        Q  \n",
       "3   315154   8.6625        S  \n",
       "4  3101298  12.2875        S  "
      ]
     },
     "execution_count": 58,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "labelencoder = LabelEncoder()\n",
    "titanic_data['Sex'] = labelencoder.fit_transform(titanic_data['Sex'])\n",
    "\n",
    "titanic_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABacAAANRCAYAAAD3YgA3AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAABYlAAAWJQFJUiTwAAA/u0lEQVR4nO3deZDnVX3v/9d7GEAZh2FTwAsKQUBcUCEqi1dZbgjGBVDcMMKY6L3ugEuupaKDN95KInFDjT+NCooKFkYQFyTKLouR1YVFllHJFReGwYEBFOb8/uhvk56enr3ndPf041HV9env+WznQ1eZqWd9cr7VWgsAAAAAAPQ0Y6InAAAAAADA9CNOAwAAAADQnTgNAAAAAEB34jQAAAAAAN2J0wAAAAAAdCdOAwAAAADQnTgNAAAAAEB34jQAAAAAAN2J0wAAAAAAdCdOAwAAAADQnTgNAAAAAEB34jQAAAAAAN3NnOgJTEdVdWuSTZPMn+CpAAAAAACsjR2S/KG1tuPqnihOT4xNH/7wh2+x2267bTHREwEAAAAAWFPXXXdd7r333jU6V5yeGPN32223La644oqJngcAAAAAwBrbc889c+WVV85fk3OtOQ0AAAAAQHfiNAAAAAAA3YnTAAAAAAB0J04DAAAAANCdOA0AAAAAQHfiNAAAAAAA3YnTAAAAAAB0N3OiJwAAAAAATE9LlizJggULsmjRotx///1prU30lKa1qsrGG2+c2bNnZ4sttsiMGev23WZxGgAAAADobsmSJfnVr36VxYsXT/RUGGit5b777st9992Xe+65J9tvv/06DdTiNAAAAADQ3YIFC7J48eLMnDkz22yzTWbNmrXO39RlxZYsWZJ77rknt99+exYvXpwFCxZkq622Wmf389cGAAAAALpbtGhRkmSbbbbJ7NmzhelJYMaMGZk9e3a22WabJP/1N1pn91unVwcAAAAAGMP999+fJJk1a9YEz4TRhv8mw3+jdUWcBgAAAAC6G/7yQ29MTz5VlSTr/Asq/eUBAAAAAHjIcJxe18RpAAAAAAC6E6cBAAAAAOhOnAYAAAAAGEcnnXRSqionnXTSRE/lIZNxTuI0AAAAADCpPfjgg/nMZz6T5zznOdliiy2y4YYb5lGPelR23333vOY1r8k3vvGNiZ4ia2DmRE8AAAAAAGB5HnzwwTz/+c/P2Wefnc022yzPe97zst122+WPf/xjfvrTn+bLX/5yrr/++rzwhS+c6Kk+5LDDDstee+2VbbfddqKnMqmJ0wAAAADApPWVr3wlZ599dp7ylKfkggsuyJw5c5bav3jx4lx++eUTNLuxzZkzZ5l5sizLegAAAAAAk9Yll1ySJJk7d+6YwXeTTTbJ/vvv/9DnefPmpapy/vnnL3Ps/PnzU1WZO3fuUuNz585NVeWWW27JiSeemN133z0Pf/jDs99+++XUU09NVeXYY48dc373339/Nt9882y77bZ54IEHkiy7vvN9992XzTbbLI961KMeOma017/+9amqfPOb31xq/Prrr8/cuXOz/fbbZ6ONNsrWW2+dI444IjfccMOY17npppvykpe8JJtvvnlmzZqVffbZJ9/61rfGPHaiidMAAAAAwKS15ZZbJkluvPHGdX6vo48+Oscdd1ye/OQn5+ijj86+++6bQw89NHPmzMmXv/zlMcPymWeemYULF+aVr3xlZs4ce6GKhz3sYXnZy16W3/3ud/nOd76zzP77778/p512WrbeeuscfPDBD42fffbZ2WOPPfKlL30pT3/603PMMcfkwAMPzL/927/lGc94Rq688sqlrvPzn/88e+21V04//fTsvffeOfroo7Pddtvl0EMPzb/927+t5X+d8WdZDwAAAABg0nrRi16Uf/zHf8ynPvWpLFq0KIcddlj23HPPPPaxjx33e1155ZW56qqrsuOOOy41/rKXvSyf/vSnc/bZZ+f5z3/+UvtOPvnkJMlRRx21wmvPnTs3n/70p3PyySfnBS94wVL7vvGNb+TOO+/MW9/61ocC95133plXvOIV2WSTTXLhhRfmCU94wkPH/+QnP8lee+2V17zmNUsF6je+8Y2544478pGPfCRHH330Q+NnnnlmDj300FX/D9GJN6cBAAAAgEnraU97Wk455ZRsvfXWOeWUU/LiF784O+ywQ7bccsscdthhOeuss8btXn/3d3+3TJhO/is8D4foYbfffnu++93v5mlPe1qe/OQnr/Dae++9d3bZZZecddZZWbBgwVL7xgrcX/jCF7Jw4cIcf/zxS4XpJHnSk56U1772tbnqqqvys5/9LEly22235d///d+z44475k1vetNSxx9yyCF5znOes8L5TQRvTgMAAAAAk9pLX/rSHHbYYTnvvPNy8cUX56qrrsrFF1+cM844I2eccUaOPPLIh9Z5XhvPeMYzxhzfZ599HgrLd955ZzbffPMkyZe+9KU8+OCDy6xhvTxHHXVU3v3ud+fUU0/NG97whiTJb37zm4cC9+677/7QsZdeemmS5Jprrsm8efOWudbwMifXXXddnvCEJ+Sqq65KkjzrWc/KBhtssMzx++23Xy644IJVmmcv4jQAAAAAMOltuOGGOeigg3LQQQclSR588MF87Wtfy9/8zd/kC1/4Qg477LC1Xrpim222We6+kWH59a9/fZKhN5433HDDHHHEEat0/SOPPDLHHXdcTj755Ifi9Je+9KU88MADyywLcscddyRJPvOZz6zwmnfffXeS5K677kqSbL311mMet6JnmyiW9QAAAAAAppwNNtggL33pS3PssccmSc4999wkyYwZQ8lzrC8vXLhw4QqvuaI3r1/1qldlxowZDy3BcdVVV+XHP/5x/uqv/ipbbbXVKs15u+22ywEHHJAf/vCHuf7665MsP3DPmTMnydCb06215f4MR+3h43/zm9+Mee/bb799lebYkzgNAAAAAExZs2fPTpK01pLkoSU3fvWrXy1z7I9+9KM1vs/222+fAw44IJdffnluuOGGVf4ixNGGlwA5+eSTc/XVV+faa6/Nc5/73DzykY9c6ri99torSXLRRRet0nWf9rSnJUkuvvjiPPjgg8vsP//881drnj2I0wAAAADApPWVr3wl//7v/54lS5Yss+/2229/aNmLZz/72Un+a93oz3/+80u9Pf2rX/0q73//+9dqLsNh+bOf/Wy+8pWvZKuttsrzn//81brGi170omy66aY55ZRTctJJJy113ZFe/epXZ7PNNsvxxx+fH/7wh8vsX7JkyVLBebvttstf/MVf5NZbb83HP/7xpY4988wzJ91604k1pwEAAACASezyyy/PRz/60WyzzTZ51rOelR133DFJcuutt+Zb3/pW7r333hxyyCE5/PDDkyTPfOYz8+xnPzsXXnhhnvGMZ+SAAw7Ib37zm5x11ln5y7/8yzHfqF5Vhx12WDbddNN85CMfyZ/+9Ke8+c1vzoYbbrha13j4wx+el7zkJfnsZz+bT37yk9lyyy3zvOc9b5njttxyy5x++uk57LDDstdee+XAAw/ME5/4xFRVfvWrX+XSSy/NHXfckfvuu++hcz7xiU9k7733zjHHHJNzzjknT3nKU3LTTTfl61//el7wghfkrLPOWuNnXxfEaQAAAABg0nrb296WnXfeOd/73vdy7bXX5rvf/W7uu+++bLnlltlvv/1yxBFH5Igjjlhqvegzzzwz73jHO3LmmWfmxBNPzM4775x/+qd/ykEHHZSvfvWrazyXTTbZ5KGwnKz+kh7D5s6dm89+9rP505/+lFe84hXZaKONxjzuwAMPzLXXXpsTTjgh3/3ud3PRRRdlo402yqMf/egccMABefGLX7zU8TvvvHMuu+yyvPOd78z3vve9nH/++dl9991zxhln5He/+92ki9M1vBYL/VTVFXvsscceV1xxxURPBQAAAAAmxHXXXZck2W233SZ4JoxlVf8+e+65Z6688sorW2t7ru49rDkNAAAAAEB34jQAAAAAAN1ZcxoAAFjv7fmOL0z0FIAp4ooPHjnRUwCYNrw5DQAAAABAd+I0AAAAAADdidMAAAAAAHQnTgMAAAAA0J04DQAAAABAd+I0AAAAAADdidMAAAAAAHQnTgMAAAAA0J04DQAAAABAd+I0AAAAAADdidMAAAAAAHQ3c6InAAAAAACwNvZ8xxcmegordMUHjxy3a912221573vfm7PPPjt33HFHtt122xx66KF53/vel80333zc7tODOA0AAAAAMAXcfPPN2WefffLb3/42hxxySB7/+Mfnhz/8YT760Y/m7LPPzg9+8INsueWWEz3NVWZZDwAAAACAKeANb3hDfvvb3+ZjH/tYzjjjjPzDP/xDzj333Bx77LG54YYb8u53v3uip7haxGkAAAAAgEnu5ptvzjnnnJMddtghb3zjG5fad/zxx2fWrFn54he/mHvuuWeCZrj6xGkAAAAAgEnuvPPOS5IcdNBBmTFj6aw7e/bs7Lvvvlm8eHEuu+yyiZjeGhGnAQAAAAAmuRtuuCFJsssuu4y5f+edd06S3Hjjjd3mtLbEaQAAAACASe6uu+5KksyZM2fM/cPjCxcu7DWltSZOAwAAAADQnTgNAAAAADDJDb8ZPfwG9WjD45tttlmvKa01cRoAAAAAYJLbddddkyx/Temf//znSZa/JvVkJE4DAAAAAExy+++/f5LknHPOyZIlS5bat2jRovzgBz/IJptskr322msiprdGxGkAAAAAgElup512ykEHHZT58+fnE5/4xFL73ve+9+Wee+7Jq171qsyaNWuCZrj6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",
      "text/plain": [
       "<Figure size 864x504 with 1 Axes>"
      ]
     },
     "execution_count": 60,
     "metadata": {
      "image/png": {
       "height": 424,
       "width": 723
      },
      "needs_background": "light"
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sns.countplot(x=titanic_data['Sex'],hue=titanic_data['Survived'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "#### Drop unneccasey column for modeling\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "collapsed": true,
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "\"['PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Fare'] not found in axis\"",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_266/3539088817.py\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mtitanic_data\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"PassengerId\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"Name\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"SibSp\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"Parch\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"Ticket\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"Fare\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"Age\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"Embarked\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0minplace\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/frame.py\u001b[0m in \u001b[0;36mdrop\u001b[0;34m(self, labels, axis, index, columns, level, inplace, errors)\u001b[0m\n\u001b[1;32m   5256\u001b[0m                 \u001b[0mweight\u001b[0m  \u001b[0;36m1.0\u001b[0m     \u001b[0;36m0.8\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   5257\u001b[0m         \"\"\"\n\u001b[0;32m-> 5258\u001b[0;31m         return super().drop(\n\u001b[0m\u001b[1;32m   5259\u001b[0m             \u001b[0mlabels\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlabels\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   5260\u001b[0m             \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36mdrop\u001b[0;34m(self, labels, axis, index, columns, level, inplace, errors)\u001b[0m\n\u001b[1;32m   4547\u001b[0m         \u001b[0;32mfor\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlabels\u001b[0m \u001b[0;32min\u001b[0m \u001b[0maxes\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mitems\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4548\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mlabels\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 4549\u001b[0;31m                 \u001b[0mobj\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_drop_axis\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlevel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlevel\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   4550\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4551\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0minplace\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36m_drop_axis\u001b[0;34m(self, labels, axis, level, errors, only_slice)\u001b[0m\n\u001b[1;32m   4589\u001b[0m                 \u001b[0mnew_axis\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlevel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlevel\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4590\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 4591\u001b[0;31m                 \u001b[0mnew_axis\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   4592\u001b[0m             \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_indexer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnew_axis\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4593\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mdrop\u001b[0;34m(self, labels, errors)\u001b[0m\n\u001b[1;32m   6697\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mmask\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0many\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   6698\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0merrors\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;34m\"ignore\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 6699\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"{list(labels[mask])} not found in axis\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   6700\u001b[0m             \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mindexer\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m~\u001b[0m\u001b[0mmask\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   6701\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdelete\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mindexer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: \"['PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Fare'] not found in axis\""
     ]
    }
   ],
   "source": [
    "titanic_data.drop(columns=[\"PassengerId\",\"Name\",\"SibSp\",\"Parch\",\"Ticket\",\"Fare\",\"Age\", \"Embarked\"],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Survived  Pclass  Sex\n",
       "0         0       3    1\n",
       "1         1       3    0\n",
       "2         0       2    1\n",
       "3         0       3    1\n",
       "4         1       3    0"
      ]
     },
     "execution_count": 88,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "## Modeling\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "X=titanic_data[['Sex', 'Pclass']]\n",
    "Y=titanic_data['Survived']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "##### Split data into test and train by using Sklearn library\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "#### Create training Model\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-2 {color: black;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression(random_state=0)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression(random_state=0)</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LogisticRegression(random_state=0)"
      ]
     },
     "execution_count": 76,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import accuracy_score,precision_score,confusion_matrix\n",
    "log = LogisticRegression(random_state = 0)\n",
    "log.fit(X_train, Y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "#### create Prediction model\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1,\n",
       "       0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1,\n",
       "       0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1,\n",
       "       1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0])"
      ]
     },
     "execution_count": 77,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred = log.predict(X_test)\n",
    "pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy_score : 1.0\n",
      "Matrix : [[45  0]\n",
      " [ 0 39]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Accuracy_score :\", accuracy_score(Y_test, pred))\n",
    "print(\"Matrix :\",confusion_matrix(Y_test,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "360    0\n",
       "170    0\n",
       "224    1\n",
       "358    0\n",
       "309    1\n",
       "      ..\n",
       "100    1\n",
       "7      0\n",
       "22     1\n",
       "68     0\n",
       "328    0\n",
       "Name: Survived, Length: 84, dtype: int64"
      ]
     },
     "execution_count": 72,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "submission=X.iloc[:,:].values\n",
    "y_final=log.predict(submission)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(418,)"
      ]
     },
     "execution_count": 92,
     "metadata": {
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_final.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "final = pd.DataFrame()\n",
    "final[\"Sex\"]= X['Sex']\n",
    "final[\"survived\"]=y_final"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
    "final.to_csv(\"submission.csv\",index=False)|"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "##### Trainig is completed, now check\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "#### predict\\(\\[\\[ Pclass, Sex \\]\\]\\) =&gt; survived or not survived\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "So soory, Not Survived\n"
     ]
    }
   ],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "result = log.predict([[5,0]])\n",
    "if(result == 0):\n",
    "    print(\"So soory, Not Survived\")\n",
    "else:\n",
    "    print(\"Survived\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
   ],
   "source": [
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "argv": [
    "/usr/bin/python3",
    "-m",
    "ipykernel",
    "--HistoryManager.enabled=False",
    "--matplotlib=inline",
    "-c",
    "%config InlineBackend.figure_formats = set(['retina'])\nimport matplotlib; matplotlib.rcParams['figure.figsize'] = (12, 7)",
    "-f",
    "{connection_file}"
   ],
   "display_name": "Python 3 (system-wide)",
   "env": {
   },
   "language": "python",
   "metadata": {
    "cocalc": {
     "description": "Python 3 programming language",
     "priority": 100,
     "url": "https://www.python.org/"
    }
   },
   "name": "python3",
   "resource_dir": "/ext/jupyter/kernels/python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}