# Project Overview

## Project Schedule

This schedule will be used to keep track of your progress throughout the week and align with our expectations.

You are **responsible** for scheduling time with your squad to seek approval for each deliverable by the end of the corresponding day, excluding `Saturday` and `Sunday`.

| Day   | Deliverable                                          | Status     |
| ----- | ---------------------------------------------------- | ---------- |
| Day 1 | Project Description                                  | Complete   |
| Day 1 | Wireframes / Priority Matrix / Functional Components | Complete   |
| Day 2 | Core Application Structure (HTML, CSS, etc.)         | Complete   |
| Day 3 | Pseudocode / actual code                             | Complete   |
| Day 3 | Initial Clickable Model                              | Complete   |
| Day 4 | MVP                                                  | Complete   |
| Day 5 | Present                                              | Incomplete |

## Project Description

This app keeps track of all expenses and incomes and see the balance you have at the moment.

## [Wireframes](https://photos.app.goo.gl/BWXa42kUcKHUA1aG7)

[Link to Wireframes](https://photos.app.goo.gl/BWXa42kUcKHUA1aG7)

## [Priority Matrix](https://photos.app.goo.gl/bnLUxTuaLBdyW4US9)

[Link to Priority Matrix](https://photos.app.goo.gl/bnLUxTuaLBdyW4US9)

## [ERD](https://photos.app.goo.gl/SWXnxWQW6kmUdFLN7)

[Link to ERD](https://photos.app.goo.gl/SWXnxWQW6kmUdFLN7)

### MVP/PostMVP - 5min

The functionality will then be divided into two separate lists: MPV and PostMVP. Carefully decided what is placed into your MVP as the client will expect this functionality to be implemented upon project completion.

#### MVP

- The user can insert incomes. &#10003;
- The user can insert expenses. &#10003;
- The user can delete incomes. &#10003;
- The user can delete expenses. &#10003;
- The user can see their balance. &#10003;
- The user can see the transaction details. &#10003;

#### PostMVP

- User login. &#10003;
- Image uploading.
- History.
- Session handling.
- Edit incomes. &#10003;
- Edit expenses. &#10003;
- search. &#10003;
- Date filter. &#10003;
- Dom Virtualization.

## [React Architectural Design](https://photos.app.goo.gl/y5c3GFojTMtRKcVj6)

[Link to React Architectural Design](https://photos.app.goo.gl/y5c3GFojTMtRKcVj6)

## UI Components

Based on the initial logic defined in the previous sections try and breakdown the logic further into stateless/stateful components.

| Component          |                      Description                       |
| ------------------ | :----------------------------------------------------: |
| App                |              Serves as a main container.               |
| HeaderComponent    | Renders the username, user balance and log out button. |
| LogIn              |                      Log in form                       |
| SignUp             |                   Creates a new user                   |
| Transaction        |              Renders a single transaction              |
| TransactionDetails |             Gives you transaction details              |
| TransactionForm    |            Creates or updates a transaction            |

## Time Frames

Time frames are also key in the development cycle. You have limited time to code all phases of the game. Your estimates can then be used to evalute game possibilities based on time needed and the actual time you have before game must be submitted. It's always best to pad the time by a few hours so that you account for the unknown so add and additional hour or two to each component to play it safe.

| Component                                | Priority | Estimated Time | Actual Time |
| ---------------------------------------- | :------: | :------------: | :---------: |
| HTML/CSS                                 |    H     |      7hrs      |    8hrs     |
| The user can insert incomes              |    H     |      7hrs      |    7hrs     |
| The user can insert expenses             |    H     |      3hrs      |    6hrs     |
| The user can delete incomes              |    H     |      5hrs      |    4hrs     |
| The user can delete expenses             |    H     |      3hrs      |    1hrs     |
| The user can see their balance           |    H     |      2hrs      |    2hrs     |
| The user can see the transaction details |    M     |      5hrs      |    4hrs     |
| PostMVPs                                 |    L     |     20hrs      |    15hrs    |
| Total                                    |          |     52hrs      |    47hrs    |

## Helper Functions

Helper functions should be generic enought that they can be reused in other applications. Use this section to document all helper functions that fall into this category.

| Function | Description |
| -------- | :---------: |


## Additional Libraries

Use this section to list all supporting libraries and thier role in the project.

| Library           |             What it Does              |
| ----------------- | :-----------------------------------: |
| React             |  Control the view in your front end   |
| Semantic UI       |       For a responsive approach       |
| Django            |  Back-end framework built in Python   |
| react-cookie      |      Work with cookies in react       |
| semantic-ui-react | Oficial Semantic UI library for react |
| semantic-ui-css   |        Give the Semantic style        |

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description

```
const [isOpen, setIsOpen] = useState(false);
// this function add commas as a separator in numbers.
// source: React official website

```

```
const actualDateTimeInput = () => {
  const dateTimeArray = new Date().toISOString().split(".");
  dateTimeArray.pop();

  return dateTimeArray.join("");
};
//Use to format time
```

## Change Log

Use this section to document what changes were made and the reasoning behind those changes.

| Original Plan |                    Outcome                    |
| ------------- | :-------------------------------------------: |
| Use Boostrap  | Use Semantic UI to know another CSS Framework |

## Issues and Resolutions

Use this section to list of all major issues encountered and their resolution.

**ERROR**: Map returning to default when zooming in or out.
**RESOLUTION**: adding the previous state to the onViewPortChange event.

```

```
